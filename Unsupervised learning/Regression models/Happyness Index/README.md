
# 🧠 Happiness Predictor Web Application

A lightweight, interactive web application built using **Flask** and **scikit-learn** that predicts an individual's happiness score based on their income. This application utilizes a **Linear Regression** model and is fully deployable on **Render**.

Live Demo:https://machine-learning-projects-d0gh.onrender.com
---

## ✨ Features

* 🔍 Predict happiness based on income
* 🧠 Machine Learning model built with `scikit-learn`
* 🌐 Frontend using HTML and CSS
* ⚙️ Backend using Flask
* ☁️ Cloud deployment ready (Render-compatible)

---

## 📁 Project Structure

```
happiness-predictor/
│
├── app.py                 # Main Flask application
├── model.pkl              # Pre-trained Linear Regression model
├── requirements.txt       # Python dependencies
├── render.yaml            # Deployment configuration for Render
│
├── templates/
│   └── index.html         # Frontend HTML
│
└── static/
    └── style.css          # CSS styling
```

---

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git
cd "Regression models/Happyness Index"
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application Locally

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the app.

---

## 🧠 Model Overview

This project uses a simple **Linear Regression** model trained on sample data to predict happiness scores based on income.

---

## ☁️ Deployment on Render

1. **Create `render.yaml`**

```yaml
services:
  - type: web
    name: happiness-predictor
    env: python
    buildCommand: ""
    startCommand: gunicorn app:app
    plan: free
    region: oregon
```

2. **Push your project to GitHub**

3. **Deploy to Render**

   * Go to [Render.com](https://render.com)
   * Click **“New Web Service”**
   * Connect your GitHub repository
   * Set **Root Directory**: `Regression models/Happyness Index`
   * Start command: `gunicorn app:app`
   * Environment: Python
   * Render will automatically build and deploy your app

**Live App:** [https://machine-learning-projects-d0gh.onrender.com/predict](https://machine-learning-projects-d0gh.onrender.com/predict)

---

## ✅ Requirements

```txt
Flask==2.3.3
gunicorn==21.2.0
scikit-learn==1.4.2
numpy==1.26.4
```

---

## 🔒 Security Notes

* Minimal input validation is included. For production, consider sanitizing inputs more thoroughly.
* Avoid using `pickle` with untrusted data sources.

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

**Awab Idris**
GitHub: [@Pinkkygold](https://github.com/Pinkkygold)
LinkedIn: [Awab Idris](https://www.linkedin.com/in/awab-abdalla)



