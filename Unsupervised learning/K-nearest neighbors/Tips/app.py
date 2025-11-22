import os
import pickle
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

MODEL_PATH = "tips_knn_model.pkl"

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    predicted_tip = None
    tip_percent = None
    input_values = {}

    # Default example values
    default_values = {
        "total_bill": 50.0,
        "sex": "Female",
        "smoker": "No",
        "day": "Sat",
        "time": "Dinner",
        "size": 3,
    }

    if request.method == "POST":
        def get_num(name, default, cast=float):
            val = request.form.get(name, "").strip()
            if val == "":
                return cast(default)
            try:
                return cast(val)
            except ValueError:
                return cast(default)

        input_values = {
            "total_bill": get_num("total_bill", default_values["total_bill"], float),
            "sex": request.form.get("sex", default_values["sex"]),
            "smoker": request.form.get("smoker", default_values["smoker"]),
            "day": request.form.get("day", default_values["day"]),
            "time": request.form.get("time", default_values["time"]),
            "size": get_num("size", default_values["size"], int),
        }

        # DataFrame with same structure as training
        new_data = pd.DataFrame(
            {
                "total_bill": [input_values["total_bill"]],
                "sex": [input_values["sex"]],
                "smoker": [input_values["smoker"]],
                "day": [input_values["day"]],
                "time": [input_values["time"]],
                "size": [input_values["size"]],
            }
        )

        # Predict tip
        pred = model.predict(new_data)[0]
        predicted_tip = round(float(pred), 2)

        if input_values["total_bill"] > 0:
            tip_percent = round(predicted_tip / input_values["total_bill"] * 100, 2)

    else:
        input_values = default_values

    return render_template(
        "index.html",
        predicted_tip=predicted_tip,
        tip_percent=tip_percent,
        input_values=input_values,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port, debug=True)
