import os
import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the trained model (Sklearn/Imblearn Pipeline)
MODEL_PATH = "Emotions_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probabilities = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("text", "").strip()

        if user_text:
            # Model expects iterable of texts
            pred = model.predict([user_text])[0]
            prediction = pred

            # If probability method available, get distribution
            if hasattr(model, "predict_proba"):
                probs = model.predict_proba([user_text])[0]
                classes = list(model.classes_)
                probs_list = [
                    {"label": label, "prob": round(float(p) * 100, 2)}
                    for label, p in sorted(
                        zip(classes, probs),
                        key=lambda x: x[1],
                        reverse=True,
                    )
                ]
                probabilities = probs_list

    return render_template(
        "index.html",
        prediction=prediction,
        probabilities=probabilities,
        user_text=user_text,
    )


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """
    Simple JSON API endpoint:
    payload: {"text": "..."}
    response: {"prediction": "joy", "probabilities": [{"label": "...", "prob": ...}, ...]}
    """
    data = request.get_json(force=True, silent=True) or {}
    text = (data.get("text") or "").strip()

    if not text:
        return jsonify({"error": "No text provided"}), 400

    pred = model.predict([text])[0]

    result = {"prediction": pred, "probabilities": None}

    if hasattr(model, "predict_proba"):
        probs = model.predict_proba([text])[0]
        classes = list(model.classes_)
        probs_list = [
            {"label": label, "prob": round(float(p) * 100, 2)}
            for label, p in sorted(
                zip(classes, probs),
                key=lambda x: x[1],
                reverse=True,
            )
        ]
        result["probabilities"] = probs_list

    return jsonify(result)


if __name__ == "__main__":
    # For local dev; Render will override PORT
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
