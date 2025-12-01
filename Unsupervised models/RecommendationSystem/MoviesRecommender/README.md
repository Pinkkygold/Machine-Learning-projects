

# 🎬 Movie Recommendation System (Content-Based)

### 🔗 **Live Demo:**

👉 **[https://movierecommender-ovt8.onrender.com](https://movierecommender-ovt8.onrender.com)**

A lightweight, efficient **content-based movie recommendation system** that suggests similar movies based on:

* 🎭 **Genre similarity**
* ⭐ **Movie ratings**
* 📐 **Cosine distance + rating distance**

No machine learning model training — just pure **similarity-based recommendations**.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Recommendation-System-purple" />
  <img src="https://img.shields.io/badge/Type-Content--Based-brightgreen" />
  <img src="https://img.shields.io/badge/Framework-Flask-red?logo=flask" />
  <img src="https://img.shields.io/badge/Hosted%20On-Render-0466C8?logo=render" />
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/awab-abdalla">
    <img src="https://img.shields.io/badge/Contact-LinkedIn-blue?logo=linkedin" />
  </a>
  <a href="mailto:awab1355@gmail.com">
    <img src="https://img.shields.io/badge/Email-Me-red?logo=gmail" />
  </a>
</p>

---

## 🧠 **How It Works**

This recommender follows a simple yet effective content-based approach:

1. Extract genres from each movie and convert them to a **one-hot vector**.
2. Compute each movie's **average rating**.
3. Measure movie similarity using:

   * Cosine distance between genre vectors
   * Difference in ratings
4. Return the **closest movies** as recommendations.

No supervised algorithms — this is a **pure similarity-driven system**.

---

## 🌐 **Web App Features**

✔ Select a movie from the dropdown
✔ Instantly receive **top similar movies**
✔ Modern UI built with Flask + Jinja2
✔ Zero page reload (fast response)
✔ Fully deployed on Render

---

## 🛠️ **Tech Stack**

* **Python**
* **Flask**
* **Pandas**, **NumPy**
* **SciPy** (cosine similarity)
* **HTML / Jinja2**
* **Render** for deployment

---

## 📁 **Dataset**

Uses MovieLens-style files:

* `movies.csv` — movie metadata (title, genres)
* `ratings.csv` — user ratings

Merged, vectorized, and used for similarity scoring.

---

## 🚀 **Live Deployment**

View the project live:

👉 **[https://movierecommender-ovt8.onrender.com](https://movierecommender-ovt8.onrender.com)**

Instant movie recommendations with no login required.

---


## 👨‍💻 **Author**

**Awab Elkhair Abdalla**

* 🌍 LinkedIn: [https://www.linkedin.com/in/awab-abdalla](https://www.linkedin.com/in/awab-abdalla)
* 📧 Email: **[awab1355@gmail.com](mailto:awab1355@gmail.com)**

If you like this project, please ⭐ the repository — it helps a lot!




