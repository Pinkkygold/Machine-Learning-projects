
# 🌸 Iris Flower Classifier

### *(Flask + Scikit-Learn + Random Forest + Render Cloud Deployment)*

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://iris-classifier-vv7m.onrender.com)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📘 Overview

**Iris Flower Classifier** is a **Machine Learning web application** that predicts the species of an Iris flower using a **Random Forest Classifier**.
Users input four numeric flower measurements (sepal length, sepal width, petal length, petal width), and the model instantly classifies the flower into:

* **Iris Setosa**
* **Iris Versicolor**
* **Iris Virginica**

Built using **Flask**, powered by **Scikit-Learn**, and fully deployed on **Render Cloud**.

> 🎯 **Live Demo:**
> 👉 [https://iris-classifier-vv7m.onrender.com](https://iris-classifier-vv7m.onrender.com)

---

## 🚀 Key Features

✅ **High-Accuracy ML Model** — Random Forest trained on the classic Iris dataset
✅ **Instant Predictions** — Real-time flower classification
✅ **Clean and Simple UI** — Easy-to-use form interface
✅ **Educational Visual Diagram** — Shows Sepal vs Petal differences
✅ **Responsive Web App** — Works on mobile & desktop
✅ **Lightweight Deployment** — Hosted on Render Cloud
✅ **No Dependencies Needed** — Everything runs server-side

---

## 🧠 Machine Learning Model

* **Algorithm:** Random Forest Classifier
* **Dataset:** Iris Dataset (150 samples, 4 features)
* **Classes:** Setosa, Versicolor, Virginica
* **Target Variable:** `species`

### Model Configuration:

| Component            | Description                             |
| -------------------- | --------------------------------------- |
| **Train/Test Split** | 80% training, 20% testing               |
| **Accuracy**         | ~98–100% depending on seed              |
| **Preprocessing**    | Duplicate removal, correlation heatmaps |
| **Model Export**     | Pickle file: `RandomForst-IRIS.pkl`     |

---

## 📊 Model Performance

The Random Forest classifier demonstrates:

| Metric               | Score                         |
| -------------------- | ----------------------------- |
| **Accuracy**         | ~98%                          |
| **Precision**        | High (per-class)              |
| **Recall**           | High                          |
| **Confusion Matrix** | Nearly perfect classification |

**Takeaway:**
The Iris dataset is linearly separable → Random Forest performs exceptionally well.

---

## 🧩 Project Structure

```
iris-classifier/
│
├── app.py                         # Main Flask application
├── RandomForst-IRIS.pkl           # Trained Random Forest model
├── requirements.txt               # Python dependencies
│
├── templates/
│   ├── index.html                 # Input UI
│   └── result.html                # Prediction output page
│
└── static/
    ├── style.css                  # Styling
    └── iris_explain.png           # Educational diagram
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pinkkygold/<YOUR-REPO>.git
cd <YOUR-REPO>
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application

```bash
python app.py
```

Visit 👉 **[http://localhost:5000](http://localhost:5000)**

---

## 🎯 Usage Guide

### 🌼 Flower Prediction Workflow

1. Enter **sepal length**
2. Enter **sepal width**
3. Enter **petal length**
4. Enter **petal width**
5. Click **Predict**
6. View the predicted species + entered values

### 🌸 Educational Diagram

The homepage includes a diagram explaining:

* Sepal vs Petal
* Where each measurement is located

---

## 🌐 API Endpoints (Optional)

### Predict Flower Species

```python
import requests

data = {
    'sepal_length': 5.4,
    'sepal_width': 3.2,
    'petal_length': 4.7,
    'petal_width': 1.4
}

response = requests.post('https://iris-classifier-vv7m.onrender.com/predict', data=data)
print(response.text)
```

---

## 🚀 Deployment on Render

### Build Command:

```bash
pip install -r requirements.txt
```

### Start Command:

```bash
gunicorn app:app
```

### Environment:

* **Python Version:** 3.9+
* **Port:** `$PORT` (assigned by Render)

---

## 🛠️ Tech Stack

* **Backend:** Flask
* **Machine Learning:** Scikit-Learn
* **Data Processing:** Pandas, NumPy
* **Visualization:** Seaborn, Matplotlib
* **Frontend:** HTML5, CSS3
* **Deployment:** Render + Gunicorn
* **Model Serialization:** Pickle


---

## 👨‍💻 Author

**Awab Elkhair (Pinkkygold)**
🔬 *Machine Learning Engineer in progress*
🌍 *Building practical ML web apps*

💻 GitHub: [https://github.com/Pinkkygold](https://github.com/Pinkkygold)
🧠 ML Projects: [https://github.com/Pinkkygold/Machine-Learning-projects](https://github.com/Pinkkygold/Machine-Learning-projects)

---

## 🧾 License

This project is open-sourced under the **MIT License**.

---
