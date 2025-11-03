from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load trained model
with open('BreastCancer.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        mean_radius = float(request.form['mean_radius'])
        input_data = np.array([[mean_radius]])

        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0][1]

        if prediction == 1:
            result = f"⚠️ Malignant Tumor Detected ({proba*100:.2f}% probability)"
            color = 'red'
        else:
            result = f"✅ Benign Tumor ({(1-proba)*100:.2f}% probability)"
            color = 'green'

        return render_template('index.html', result=result, color=color)
    
    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}", color='gray')

if __name__ == '__main__':
    app.run(debug=True)
