
# 🩺 Diabetes Risk Prediction Web App (KNN + Flask)

A Machine Learning web application that predicts the risk of diabetes based on basic health metrics using a K-Nearest Neighbors (KNN) model.  
Built with Scikit-Learn, Flask, Plotly, and deployed on Render.

🔗 **Live Demo:** https://knn-diabetes.onrender.com  

---

<p align="center">
  <a href="https://knn-diabetes.onrender.com">
    <img src="https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=render" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/Model-KNN-green?style=for-the-badge&logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render" />
</p>

---

## 🖼️ Screenshot


<p align="center">
<img width="1395" height="776" alt="appScreenshot" src="https://github.com/user-attachments/assets/528d0121-8a7f-4a1b-b5db-d9e5d5ef1499" />

</p>

---

## 🚀 Features

- Predicts **high** or **low diabetes risk**  
- Displays estimated **probability of diabetes** (if `predict_proba` is available)  
- Interactive **Plotly gauge chart** to visualize probability  
- Clean web interface for entering health metrics  
- Model trained using a **K-Nearest Neighbors** algorithm  
- Fully deployed and accessible online via Render

---

## 🧠 Machine Learning Model

The application uses a KNN model trained on a diabetes dataset  
(e.g., the Pima Indians Diabetes Dataset).

### Model Workflow

1. Load and inspect dataset  
2. Preprocess and scale features  
3. Split data into training and test sets  
4. Tune K (number of neighbors)  
5. Train KNN model  
6. Export trained model:

```python
import pickle

with open("diabetesmodel.pkl", "wb") as f:
    pickle.dump(model, f)
````

This file (`diabetesmodel.pkl`) is then loaded inside `app.py` for inference.

---

## 📊 Input Features

The model expects the following inputs:

* **Pregnancies** – Number of pregnancies
* **Glucose** – Plasma glucose concentration
* **Blood Pressure** – Diastolic blood pressure (mm Hg)
* **Skin Thickness** – Triceps skin fold thickness (mm)
* **Insulin** – 2-Hour serum insulin (mu U/ml)
* **BMI** – Body Mass Index (kg/m²)
* **Diabetes Pedigree Function** – Family history score
* **Age** – Age in years

These are fed into the model in the same order as during training.

---

## 🎨 Visualizations

The app includes an interactive **Plotly gauge chart** showing:

* Predicted probability of diabetes (0–100%)
* Visual risk zones (lower vs higher probability)
* A needle indicating the current prediction

This makes the prediction easier to interpret for non-technical users.

---

## 📁 Project Structure

```text
.
├── app.py
├── diabetesmodel.pkl
├── requirements.txt
└── templates/
    └── index.html
```

* `app.py` – Flask backend and routing
* `diabetesmodel.pkl` – Saved KNN model
* `templates/index.html` – Frontend UI (form + Plotly chart)
* `requirements.txt` – Python dependencies

---

## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-diabetes-repo>.git
cd <your-diabetes-repo>
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate       # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Flask app

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

## 🌐 Deployment on Render

This app is live at:

🔗 [https://knn-diabetes.onrender.com](https://knn-diabetes.onrender.com)

To deploy it yourself:

1. Push the project to GitHub
2. Go to Render → New → Web Service
3. Connect your GitHub repo
4. Configure:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

Render will build the image, start the server, and give you a public URL.

---

## 🛠️ Tech Stack

* Python 3.x
* Flask
* Scikit-Learn (KNN)
* NumPy / Pandas / SciPy
* Plotly.js (for interactive charts)
* Gunicorn
* Render (cloud hosting)

---

## ⚠️ Disclaimer

This application is intended for **educational and demonstration purposes only**.
It is **not** a medical device and must not be used for real-world diagnosis or treatment decisions.
Always consult a licensed medical professional.

---

## ✨ Author

Created by **Awab Elkhair Abdalla Idris (Pinkkygold)**

* GitHub: [https://github.com/Pinkkygold](https://github.com/Pinkkygold)
* LinkedIn: https://github.com/Pinkkygold

If you find this project useful or inspiring, feel free to ⭐ star the repository and share it!



