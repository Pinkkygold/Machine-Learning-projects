from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("Cropmodel.pkl", "rb"))

# Load scaler
scaler = pickle.load(open("scaler.pkl", "rb"))

# Homepage
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Prediction
@app.route("/predict", methods=["POST"])
def predict():
    try:
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Make array
        features = np.array([[N, P, K, temp, humidity, ph, rainfall]])

        # Scale input
        scaled_features = scaler.transform(features)

        # Model prediction
        prediction = model.predict(scaled_features)[0]

        return render_template("result.html", prediction=prediction)

    except Exception as e:
        return render_template("result.html", prediction="Error: " + str(e))


if __name__ == "__main__":
    app.run(debug=True)
