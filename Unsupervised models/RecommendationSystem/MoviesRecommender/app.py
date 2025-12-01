import os
import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from scipy.spatial.distance import cosine

# ---------- Data loading & model preparation ----------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

movies_path = os.path.join(BASE_DIR, "movies.csv")
ratings_path = os.path.join(BASE_DIR, "ratings.csv")

movies = pd.read_csv(movies_path)
ratings = pd.read_csv(ratings_path)

# Merge and build genre list
data = pd.merge(ratings, movies, on="movieId")

unique_genres = set()
for genres in data["genres"]:
    genre_list = str(genres).split("|")
    for genre in genre_list:
        unique_genres.add(genre)

all_genres = sorted(list(unique_genres))
genre_to_index = {g: i for i, g in enumerate(all_genres)}

def genre_to_vector(genres: str) -> np.ndarray:
    """Convert a 'Action|Adventure|...' string into a one-hot vector."""
    vector = np.zeros(len(all_genres), dtype=float)
    genre_list = str(genres).split("|")
    for genre in genre_list:
        idx = genre_to_index.get(genre)
        if idx is not None:
            vector[idx] = 1.0
    return vector

# Build a dictionary: movieId -> (title, genre_vector, avg_rating)
avg_ratings = ratings.groupby("movieId")["rating"].mean()

moviedict = {}
for _, row in movies.iterrows():
    movie_id = int(row["movieId"])
    title = row["title"]
    genres = row["genres"]
    g_vec = genre_to_vector(genres)
    r_val = float(avg_ratings.get(movie_id, 0.0))
    moviedict[movie_id] = (title, g_vec, r_val)

def compute_distance(movie_a, movie_b) -> float:
    """
    movie_* is (title, genre_vector, rating_value)
    Return a single scalar: total distance.
    """
    genres_a = movie_a[1]
    genres_b = movie_b[1]
    genre_distance = cosine(genres_a, genres_b)
    rating_distance = abs(float(movie_a[2]) - float(movie_b[2]))
    total_distance = genre_distance + rating_distance
    return float(total_distance)

def get_neighbors(movie_id: int, k: int = 5):
    """KNN neighbors for an existing movie."""
    if movie_id not in moviedict:
        return []
    target = moviedict[movie_id]
    distances = []
    for mid, info in moviedict.items():
        if mid == movie_id:
            continue
        dist = compute_distance(target, info)
        distances.append((mid, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = [mid for mid, _ in distances[:k]]
    return neighbors

def get_neighbors_for_profile(profile_vec: np.ndarray,
                              profile_rating: float,
                              k: int = 5,
                              exclude_ids=None):
    """
    KNN neighbors for a virtual 'user profile' movie.
    exclude_ids: set of movieIds to NOT recommend (e.g. movies user rated).
    """
    if exclude_ids is None:
        exclude_ids = set()
    profile_movie = ("USER_PROFILE", profile_vec, profile_rating)
    distances = []
    for mid, info in moviedict.items():
        if mid in exclude_ids:
            continue
        dist = compute_distance(profile_movie, info)
        distances.append((mid, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = [mid for mid, _ in distances[:k]]
    return neighbors

# ---------- Flask app ----------

app = Flask(__name__)

# Pre-build a sorted list of (id, title) for the UI
movie_choices = sorted(
    [{"id": mid, "title": info[0]} for mid, info in moviedict.items()],
    key=lambda x: x["title"]
)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", movies=movie_choices)

@app.route("/recommend-by-movie", methods=["POST"])
def recommend_by_movie():
    movie_id = int(request.form.get("movie_id"))
    k = int(request.form.get("k", 5))

    neighbors_ids = get_neighbors(movie_id, k=k)
    base_movie = moviedict.get(movie_id)
    base_title = base_movie[0] if base_movie else "Unknown movie"

    recommendations = []
    for mid in neighbors_ids:
        title, _, avg_rating = moviedict[mid]
        recommendations.append({
            "id": mid,
            "title": title,
            "rating": round(float(avg_rating), 2)
        })

    return render_template(
        "index.html",
        movies=movie_choices,
        mode="by_movie",
        selected_movie_id=movie_id,
        base_title=base_title,
        recommendations=recommendations
    )

@app.route("/recommend-by-ratings", methods=["POST"])
def recommend_by_ratings():
    # Collect up to 3 movies and their ratings
    rated_movies = []
    for i in range(1, 4):
        mid_str = request.form.get(f"movie_{i}")
        rating_str = request.form.get(f"rating_{i}")

        if not mid_str or not rating_str:
            continue

        try:
            mid = int(mid_str)
            user_rating = float(rating_str)
        except ValueError:
            continue

        if mid in moviedict and user_rating > 0:
            rated_movies.append((mid, user_rating))

    if not rated_movies:
        # Nothing was provided; just reload page with message
        return render_template(
            "index.html",
            movies=movie_choices,
            mode="by_ratings",
            error="Please choose at least one movie and give it a rating."
        )

    # Build a weighted average genre vector from the movies the user rated
    profile_vec = np.zeros(len(all_genres), dtype=float)
    total_weight = 0.0
    for mid, user_rating in rated_movies:
        _, g_vec, _ = moviedict[mid]
        profile_vec += user_rating * g_vec
        total_weight += user_rating

    if total_weight > 0:
        profile_vec /= total_weight

    # Use the mean of user's ratings as the profile's rating value
    profile_rating = float(np.mean([r for _, r in rated_movies]))

    exclude_ids = set(mid for mid, _ in rated_movies)

    k = int(request.form.get("k", 5))
    neighbors_ids = get_neighbors_for_profile(
        profile_vec, profile_rating, k=k, exclude_ids=exclude_ids
    )

    recommendations = []
    for mid in neighbors_ids:
        title, _, avg_rating = moviedict[mid]
        recommendations.append({
            "id": mid,
            "title": title,
            "rating": round(float(avg_rating), 2)
        })

    return render_template(
        "index.html",
        movies=movie_choices,
        mode="by_ratings",
        rated_movies=rated_movies,
        recommendations=recommendations
    )

if __name__ == "__main__":
    # Local debugging
    app.run(debug=True, host="0.0.0.0", port=5001)
