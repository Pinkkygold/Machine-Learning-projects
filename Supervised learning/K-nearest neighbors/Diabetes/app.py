import os
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Path to your saved model
MODEL_PATH = "diabetesmodel.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    input_values = {}

    # Default example values (you can tweak them)
    default_values = {
        "pregnancies": 2,
        "glucose": 120,
        "blood_pressure": 70,
        "skin_thickness": 20,
        "insulin": 80,
        "bmi": 28.0,
        "dpf": 0.5,  # Diabetes Pedigree Function
        "age": 35,
    }

    if request.method == "POST":
        # Get values from form; fallback to default if empty
        def get_value(name, default):
            val_str = request.form.get(name, "").strip()
            return float(val_str) if val_str != "" else float(default)

        try:
            input_values = {
                "pregnancies": get_value("pregnancies", default_values["pregnancies"]),
                "glucose": get_value("glucose", default_values["glucose"]),
                "blood_pressure": get_value("blood_pressure", default_values["blood_pressure"]),
                "skin_thickness": get_value("skin_thickness", default_values["skin_thickness"]),
                "insulin": get_value("insulin", default_values["insulin"]),
                "bmi": get_value("bmi", default_values["bmi"]),
                "dpf": get_value("dpf", default_values["dpf"]),
                "age": get_value("age", default_values["age"]),
            }

            # IMPORTANT: this order must match the order used when training the model
            features = [
                input_values["pregnancies"],
                input_values["glucose"],
                input_values["blood_pressure"],
                input_values["skin_thickness"],
                input_values["insulin"],
                input_values["bmi"],
                input_values["dpf"],
                input_values["age"],
            ]

            pred = model.predict([features])[0]
            prediction = int(pred) if isinstance(pred, (int, float)) else pred

            if hasattr(model, "predict_proba"):
                probs = model.predict_proba([features])[0]
                # Assuming positive class is 1 (diabetes)
                if len(probs) == 2:
                    # Typically: [P(class 0), P(class 1)]
                    positive_prob = probs[1]
                else:
                    # If it's multi-class or classes are different, map by label
                    try:
                        positive_index = list(model.classes_).index(1)
                        positive_prob = probs[positive_index]
                    except Exception:
                        positive_prob = max(probs)
                probability = round(float(positive_prob) * 100, 2)

        except ValueError:
            prediction = "Invalid input: please make sure all values are numeric."
            probability = None

    else:
        input_values = default_values

    risk_label = None
    if isinstance(prediction, (int, float)):
        if prediction == 1:
            risk_label = "High risk of diabetes"
        elif prediction == 0:
            risk_label = "Low risk of diabetes"

    return render_template(
        "index.html",
        prediction=prediction,
        probability=probability,
        risk_label=risk_label,
        input_values=input_values,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
