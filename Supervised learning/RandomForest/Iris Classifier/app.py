from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model
model = joblib.load("RandomForst-IRIS.pkl")   # Your trained model

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        sl = float(request.form["sepal_length"])
        sw = float(request.form["sepal_width"])
        pl = float(request.form["petal_length"])
        pw = float(request.form["petal_width"])

        X = np.array([[sl, sw, pl, pw]])

        pred = model.predict(X)[0]
        print("Raw prediction:", pred)

        mapping = {
            "setosa": "Iris Setosa",
            "versicolor": "Iris Versicolor",
            "virginica": "Iris Virginica"
        }

        result = mapping.get(pred, pred)


        return render_template("result.html",
                               result=result,
                               sl=sl, sw=sw, pl=pl, pw=pw)

    except Exception as e:
        return render_template("result.html", result="Error: " + str(e))

if __name__ == "__main__":
    app.run(debug=True)
