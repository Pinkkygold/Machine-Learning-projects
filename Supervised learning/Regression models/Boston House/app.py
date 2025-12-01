from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import joblib
import os
import traceback

app = Flask(__name__)

# Global model variable
model = None


def load_model():
    """Load the trained model from the same directory as app.py"""
    global model
    try:
        # Build absolute path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(base_dir, "Boston_regression_model.pkl")

        # Debug info (helpful for Render logs)
        print(f"📂 Looking for model at: {model_path}")
        print(f"📁 Current working directory: {os.getcwd()}")
        print(f"📄 Files in base dir: {os.listdir(base_dir)}")

        # Load model
        model = joblib.load(model_path)
        print("✅ Boston Housing Model loaded successfully!")
        return True
    except FileNotFoundError as e:
        print(f"❌ Model file not found: {e}")
        model = None
        return False
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        traceback.print_exc()
        model = None
        return False


def predict_medv(input_features_dict):
    """Predict MEDV using the trained model"""
    global model
    try:
        if model is None:
            raise RuntimeError("Model is not loaded. Please reload the app or check deployment files.")

        feature_order = [
            'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
            'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
        ]
        
        input_array = np.array([input_features_dict[feature] for feature in feature_order]).reshape(1, -1)

        print(f"Input shape: {input_array.shape}")
        print(f"Input values: {input_array}")

        prediction = model.predict(input_array)
        print(f"Raw prediction: {prediction[0]:.2f}")

        return prediction[0]

    except Exception as e:
        print(f"Prediction error: {e}")
        traceback.print_exc()
        return None


# Load the model when the app starts (important for Render)
with app.app_context():
    load_model()


if __name__ == "__main__":
    # Ensure model is loaded before starting the server
    if model is None:
        print("⚠️ Model not loaded at startup. Please check model path.")
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5001)))


# Feature descriptions for the form
feature_descriptions = {
    'CRIM': 'Per capita crime rate by town',
    'ZN': 'Proportion of residential land zoned for lots over 25,000 sq.ft',
    'INDUS': 'Proportion of non-retail business acres per town',
    'CHAS': 'Charles River dummy variable (1 if tract bounds river; 0 otherwise)',
    'NOX': 'Nitric oxides concentration (parts per 10 million)',
    'RM': 'Average number of rooms per dwelling',
    'AGE': 'Proportion of owner-occupied units built prior to 1940',
    'DIS': 'Weighted distances to five Boston employment centres',
    'RAD': 'Index of accessibility to radial highways',
    'TAX': 'Full-value property-tax rate per $10,000',
    'PTRATIO': 'Pupil-teacher ratio by town',
    'B': '1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town',
    'LSTAT': '% lower status of the population'
}

# Default values based on your test data
feature_defaults = {
    'CRIM': 0.001,
    'ZN': 20.0,
    'INDUS': 3.0,
    'CHAS': 1,
    'NOX': 1.0,
    'RM': 5.0,
    'AGE': 22.0,
    'DIS': 4.0,
    'RAD': 2.0,
    'TAX': 300.0,
    'PTRATIO': 16.0,
    'B': 400.0,
    'LSTAT': 5.0
}

# Realistic ranges based on Boston Housing dataset
feature_ranges = {
    'CRIM': (0.0, 90.0),
    'ZN': (0.0, 100.0),
    'INDUS': (0.0, 30.0),
    'CHAS': (0, 1),
    'NOX': (0.3, 0.9),
    'RM': (3.0, 9.0),
    'AGE': (0.0, 100.0),
    'DIS': (1.0, 13.0),
    'RAD': (1.0, 25.0),
    'TAX': (180.0, 711.0),
    'PTRATIO': (12.0, 23.0),
    'B': (0.0, 400.0),
    'LSTAT': (1.0, 40.0)
}

@app.route('/')
def index():
    """Render the main input form"""
    return render_template('index.html', 
                         features=feature_descriptions,
                         defaults=feature_defaults,
                         ranges=feature_ranges)

@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Get form data
        input_features = {}
        print("Received form data:")
        for feature in feature_descriptions.keys():
            value = request.form.get(feature)
            print(f"{feature}: {value}")
            
            # Convert to appropriate type
            if feature == 'CHAS':
                input_features[feature] = int(float(value))  # Handle both "1" and "1.0"
            else:
                input_features[feature] = float(value)
        
        # Make prediction
        prediction = predict_medv(input_features)
        
        if prediction is not None:
            # MEDV is already in thousands of dollars
            predicted_price = prediction * 1000
            print(f"Final prediction: ${predicted_price:,.2f}")
            
            return render_template('result.html',
                                prediction=predicted_price,
                                input_features=input_features)
        else:
            return render_template('result.html',
                                error="Prediction failed. Please try again.")
    
    except Exception as e:
        print(f"Route error: {e}")
        import traceback
        traceback.print_exc()
        return render_template('result.html',
                            error=f"Error: {str(e)}")

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for JSON predictions"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        # Make prediction
        prediction = predict_medv(data)
        
        if prediction is not None:
            return jsonify({
                'predicted_medv': prediction,
                'predicted_price_usd': prediction * 1000,
                'status': 'success'
            })
        else:
            return jsonify({'error': 'Prediction failed'}), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    if model is not None:
        return jsonify({'status': 'healthy', 'model_loaded': True})
    else:
        return jsonify({'status': 'unhealthy', 'model_loaded': False}), 500

# Load model when app starts
if __name__ == '__main__':
    if load_model():
        app.run(debug=True, host='0.0.0.0', port=5001)
    else:
        print("❌ Failed to load model. Please check your Boston_regression_model.pkl file.")
