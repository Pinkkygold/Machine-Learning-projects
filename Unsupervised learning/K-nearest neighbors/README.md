

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/ML%20Algorithm-KNN-green?style=for-the-badge&logo=scikitlearn">
  <img src="https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Visualization-Plotly-3f4f75?style=for-the-badge&logo=plotly">
  <img src="https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render">
</p>

---

## 📂 Projects Inside This Folder

### 1️⃣ 💸 Restaurant Tip Prediction App

Predicts restaurant **tip amount** using a KNN Regression model trained on the Seaborn `tips` dataset.
Includes a dark UI + Plotly bar chart for bill vs predicted tip.

* 🌐 Live App:
  **[https://tipsamount.onrender.com](https://tipsamount.onrender.com)**

* 📁 GitHub Repo:
  **[https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/K-nearest%20neighbors/Tips](https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/K-nearest%20neighbors/Tips)**

**Features:**

* Predict tip amount
* Compute tip percentage
* Interactive Plotly bar chart
* Example presets (Simple Table / Busy Table)

---

### 2️⃣ 🩺 Diabetes Risk Prediction App

Predicts whether a person is at **high or low diabetes risk** using a KNN classifier.
Includes a Plotly gauge visualizing diabetes probability.

* 🌐 Live App:
  **[https://knn-diabetes.onrender.com](https://knn-diabetes.onrender.com)**

* 📁 GitHub Repo:
  **[https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/K-nearest%20neighbors/Diabetes](https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/K-nearest%20neighbors/Diabetes)**

**Features:**

* Predict diabetes risk
* Show probability if available
* Plotly gauge visualization
* Clean white-themed UI

---

## 🧱 Shared Tech Stack

All KNN projects follow a consistent architecture:

### 🔹 Machine Learning

* K-Nearest Neighbors (KNN)
* Scikit-Learn Pipelines
* OneHotEncoding + Standard Scaling
* Pickled model for deployment

### 🔹 Backend

* Flask framework
* Gunicorn (production server)
* JSON API endpoints (easy integration)

### 🔹 Frontend

* HTML + CSS + Jinja2 templates
* Plotly.js for interactive charts
* Clean, responsive design

### 🔹 Deployment

* Hosted on **Render Cloud**
* `requirements.txt` + `gunicorn app:app`

---

## 📁 Folder Structure

```text
K-nearest neighbors/
│
├── Diabetes/
│   ├── app.py
│   ├── diabetesmodel.pkl
│   ├── requirements.txt
│   └── templates/
│       └── index.html
│
└── Tips/
    ├── app.py
    ├── tips_knn_model.pkl
    ├── requirements.txt
    └── templates/
        └── index.html
```

---

## ▶️ How to Run Any Project Locally

```bash
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git

cd "Machine-Learning-projects/Unsupervised learning/K-nearest neighbors"

cd Tips       # or: cd Diabetes
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Then open:
`http://127.0.0.1:5000`

---

## 🌟 Why This Folder Matters

This folder is a strong demonstration of:

* End-to-end ML deployment
* Traditional ML (KNN) used in real applications
* Clean reproducible ML pipelines
* Interactive data visualization
* Full web deployment on the cloud

Perfect for:

* Machine Learning portfolios
* GitHub showcases
* Recruiters
* University applications
* Entry-level ML Engineer roles

---

## ✨ Author

Created by **Awab Elkhair Abdalla Idris (Pinkkygold)**
Machine Learning Engineer (in progress) • AI for Social Impact • UN Youth Delegate

GitHub: [https://github.com/Pinkkygold](https://github.com/Pinkkygold)
LinkedIn: www.linkedin.com/in/awab-abdalla


⭐ If these projects helped you, consider starring the repository!

---
