# 📈 Regression Models – Deployed ML Web Apps Collection

This folder contains a collection of **end-to-end Regression-based Machine Learning web applications**, each:

- Trained with **scikit-learn**
- Wrapped in a **Flask** web app
- Deployed on **Render Cloud**
- Exposed via a simple and interactive **web UI** (and in some cases, REST APIs)

Current projects in this folder:

- 🏠 **Boston House Price Prediction**
- 🚗 **Car Price Prediction**
- 🧠 **Happiness Predictor**

---

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?logo=python" />
  <img src="https://img.shields.io/badge/Framework-Flask-black?logo=flask" />
  <img src="https://img.shields.io/badge/ML-Regression%20Models-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Deployment-Render-0466C8?logo=render" />
</p>

<p align="center">
  <a href="https://github.com/Pinkkygold">
    <img src="https://img.shields.io/badge/GitHub-Pinkkygold-181717?logo=github" />
  </a>
  <a href="https://www.linkedin.com/in/awab-abdalla">
    <img src="https://img.shields.io/badge/LinkedIn-Awab%20Elkhair%20Abdalla-0A66C2?logo=linkedin" />
  </a>
</p>

---

## 🧠 Projects in This Folder

### 🏠 1. Boston House Price Prediction

> Predicts the **median house price in Boston** based on socioeconomic and environmental variables.

- **Model**: Linear Regression  
- **Dataset**: Boston Housing Dataset (Kaggle)  
- **Target**: `MEDV` – median value of owner-occupied homes in $1000s  
- **Features**: crime rate, NOX, rooms, distance to employment centers, tax rate, etc.  
- **Extras**: REST API endpoint (`/api/predict`), local testing with `test_model.py`

**Live Demo:**  
👉 https://house-price-prediction-d58i.onrender.com  

**GitHub:**  
👉 https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Supervised%20learning/Regression%20models/Boston%20House  

---

### 🚗 2. Car Price Prediction

> Predicts **car prices** based on technical specifications, brand, and performance features.

- **Model**: Linear Regression  
- **Dataset**: Car Price Assignment Dataset (205 rows, 26 features)  
- **Target**: `price` – car price in USD  
- **Key Features**: brand, engine size, horsepower, curb weight, fuel type, body style, MPG, dimensions  
- **Extras**:
  - Brand categorization (Budget / Mid-Range / Luxury)  
  - Analysis dashboard (/analyze)  
  - REST API endpoint (`/api/predict`)

**Live Demo:**  
👉 https://car-price-predictor-6t6e.onrender.com  

**GitHub:**  
👉 https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Supervised%20learning/Regression%20models/Car%20Price%20predictor  

---

### 🧠 3. Happiness Predictor Web Application

> Predicts an individual’s **happiness score** based on their **income**.

- **Model**: Linear Regression  
- **Input**: Income  
- **Output**: Predicted happiness score  
- **Focus**: Minimalist example of regression → Flask → Render pipeline

**Live Demo:**  
👉 https://machine-learning-projects-d0gh.onrender.com  

**GitHub:**  
👉 https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Supervised%20learning/Regression%20models/Happyness%20Index  

---

## 🧩 Shared Tech Stack

All regression projects in this folder use a similar stack:

- 🐍 **Python**  
- 🌐 **Flask** – web framework  
- 📈 **scikit-learn** – regression models  
- 📊 **pandas**, **NumPy** – data processing  
- 🎨 **HTML5, CSS3** (some with Bootstrap) – frontend  
- ☁️ **Render** – cloud deployment  
- 🔧 **Gunicorn** – WSGI server  
- 💾 **pickle / joblib** – model serialization  

---

## 🗂️ Suggested Folder Layout

```bash
Regression models/
│
├── Boston House/
│   ├── app.py
│   ├── Boston_regression_model.pkl
│   ├── HousingData.csv
│   ├── templates/
│   ├── static/
│   └── README.md
│
├── Car Price predictor/
│   ├── app.py
│   ├── Car_price_model.pkl
│   ├── CarPrice_Assignment.csv
│   ├── templates/
│   ├── static/
│   └── README.md
│
└── Happyness Index/
    ├── app.py
    ├── model.pkl
    ├── templates/
    ├── static/
    └── README.md
````

Each project is self-contained with its own app, model, and documentation.

---

## 🎯 What You Can Learn from This Folder

By exploring these apps, you can practice:

* Building **regression models** with scikit-learn
* Exporting trained models and loading them in production
* Creating **Flask**-based ML APIs and web interfaces
* Deploying real ML systems on **Render**
* Designing small but meaningful ML apps around real-world problems

  * Housing affordability
  * Vehicle pricing
  * Income vs happiness

---

## 👨‍💻 Author

**Awab Elkhair Abdalla**
AI & Machine Learning Enthusiast · Researcher · Volunteer

* 💻 GitHub: [Pinkkygold](https://github.com/Pinkkygold)
* 🌍 LinkedIn: [awab-abdalla](https://www.linkedin.com/in/awab-abdalla)

> “Building intelligent systems that make complex decisions understandable and accessible.”

---

## ⭐ Support & Contributions

If you find these projects helpful:

* ⭐ Star the repository
* 🍴 Fork the projects and experiment with new models
* 📨 Open issues or suggestions for new regression apps

Your support helps keep more **open-source ML apps** coming 🚀
