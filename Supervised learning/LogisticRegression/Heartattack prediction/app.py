from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load the model (trained only on "age")
with open('Heartattack.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        input_data = np.array([[age]])

        # Prediction & probability
        pred = model.predict(input_data)[0]
        prob = model.predict_proba(input_data)[0][1]

        if pred == 1:
            result = f"⚠️ High Risk of Heart Attack ({prob*100:.2f}% probability)"
            color = 'red'
        else:
            result = f"✅ Low Risk ({(1-prob)*100:.2f}% probability)"
            color = 'green'

        return render_template('index.html', result=result, color=color)
    
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}", color='gray')

if __name__ == '__main__':
    app.run(debug=True)
