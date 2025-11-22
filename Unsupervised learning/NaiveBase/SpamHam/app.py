import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model (the Pipeline from your notebook)
# Make sure SpamHam_model.pkl is in the same folder as app.py
with open("SpamHam_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("message", "").strip()

        if user_text:
            # Model expects a list/array of texts
            pred = model.predict([user_text])[0]

            # Get probability if available
            if hasattr(model, "predict_proba"):
                probs = model.predict_proba([user_text])[0]
                classes = list(model.classes_)
                # Map label -> probability
                prob_dict = {label: prob for label, prob in zip(classes, probs)}
                prob_for_pred = prob_dict.get(pred, None)
                if prob_for_pred is not None:
                    probability = round(prob_for_pred * 100, 2)

            prediction = pred
        else:
            prediction = "Please enter a message to classify."

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        user_text=user_text,
    )


if __name__ == "__main__":
    # For Render: listen on 0.0.0.0 and use PORT env var
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
