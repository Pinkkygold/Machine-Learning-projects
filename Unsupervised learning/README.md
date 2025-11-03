
# 🎗️ Simple Breast Cancer Predictor

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5.0-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://simple-breast-cancer-predictor.onrender.com)

> A lightweight, interactive **machine learning web app** that predicts whether a **breast tumor** is *benign* or *malignant* based on the **mean radius** feature.  
> Built with *Flask* and *Logistic Regression*, deployed on **Render Cloud**.

🔗 **Live Demo:**  
👉 [https://simple-breast-cancer-predictor.onrender.com](https://simple-breast-cancer-predictor.onrender.com)

---

## 🧠 Overview

This project is a practical demonstration of how a **simple logistic regression model** can be deployed as a web application.  
By inputting one key feature — **mean radius** — the app predicts whether the tumor is **benign** or **malignant**, along with the prediction probability.

Even though it’s a one-feature model, it showcases the full **end-to-end machine learning lifecycle**:
- Data preprocessing & model training  
- Model serialization using `pickle`  
- Web interface with Flask  
- Cloud deployment on Render with Gunicorn

---

## 🧩 Tech Stack

| Component | Technology |
|:-----------|:------------|
| **Language** | Python |
| **Framework** | Flask |
| **Machine Learning** | Logistic Regression (`scikit-learn`) |
| **Frontend** | HTML5, CSS3 |
| **Deployment** | Render Cloud |
| **WSGI Server** | Gunicorn |

---

## 🖼️ Screenshot Preview


<p align="center">
  <img src="static/preview.png" alt="Breast Cancer Predictor Screenshot" width="80%">
</p>


---

## ⚙️ Local Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Pinkkygold/simple-breast-cancer-predictor.git
cd simple-breast-cancer-predictor
````

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate     # Mac/Linux
.venv\Scripts\activate        # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App Locally

```bash
python app.py
```

or with Gunicorn:

```bash
gunicorn app:app --bind 0.0.0.0:5000
```

Then visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧮 Project Structure

```
simple-breast-cancer-predictor/
│
├── app.py                   # Flask application
├── BreastCancer.pkl         # Trained logistic regression model
├── requirements.txt         # Project dependencies
├── Procfile                 # Start command for Render
│
├── static/
│   ├── style.css            # Frontend styling
│   └── preview.png          # Optional screenshot
│
└── templates/
    └── index.html           # Web page interface
```

---

## 🧬 Model Details

* **Algorithm:** Logistic Regression
* **Feature Used:** `mean radius`
* **Output Classes:**

  * `1` → ⚠️ *Malignant Tumor*
  * `0` → ✅ *Benign Tumor*
* **Prediction Output:** Probability score (from the logistic sigmoid function)
* **Purpose:** Demonstrate how a single feature can still provide valuable insights for early cancer screening research.

---

## 🚀 Deployment on Render

1. Push the repo to GitHub
2. Connect it to [Render](https://render.com)
3. Create a new **Web Service**
4. Use the following **Start Command**:

   ```
   gunicorn app:app
   ```
5. Render automatically installs dependencies, builds, and deploys your Flask app live 🌍

---

## 🧑‍💻 Author

**Awab Elkhair**
📍 *Machine Learning Engineer · Researcher · Volunteer*
🌐 [ResearchGate](https://www.researchgate.net/profile/Awab-Abdalla)
💼 [GitHub: Pinkkygold](https://github.com/Pinkkygold)
📫 *“Turning data into decisions that save lives.”*

---

## 🪶 License

This project is licensed under the **MIT License** — feel free to fork, modify, and use it for learning or research.

---

### ⭐ If you like this project,

Show some ❤️ by giving it a **star** on GitHub — it helps support open, educational ML projects!

