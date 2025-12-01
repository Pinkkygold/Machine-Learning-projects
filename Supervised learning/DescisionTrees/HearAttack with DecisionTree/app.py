from flask import Flask, render_template, request
import pickle
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import os

app = Flask(__name__)

# Load trained model
with open('RiskOfCHD_DecisionTree.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form
        features = [float(request.form[key]) for key in request.form]
        final_input = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(final_input)[0]

        # Dummy data for confusion matrix example
        # In real usage, replace this with actual y_test and y_pred arrays
        y_true = [0, 1, 0, 1, 1, 0, 0, 1]
        y_pred = [0, 1, 0, 1, 0, 0, 1, 1]
        cm = confusion_matrix(y_true, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                      display_labels=['No Disease', 'Disease'])

        # Plot and save confusion matrix
        plot_path = os.path.join('static', 'confusion_matrix.png')
        disp.plot(cmap='Purples', colorbar=False)
        plt.title("Confusion Matrix")
        plt.savefig(plot_path)
        plt.close()

        result_text = "✅ Not Likely to Have Heart Disease" if prediction == 0 else "⚠️ Likely to Have Heart Disease"

        return render_template('index.html', prediction=result_text, image_path=plot_path)

    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
