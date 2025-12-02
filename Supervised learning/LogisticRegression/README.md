# 📊 Logistic Regression – Mini ML Apps Collection

A collection of **lightweight, end-to-end Logistic Regression projects**, each fully deployed as an interactive web app using **Flask** and **Render**.

This folder currently includes:

- 🎗️ **Simple Breast Cancer Predictor**
- ❤️ **Simple Heart Attack Predictor**

Each project:
- Trains a **Logistic Regression** model using scikit-learn  
- Serializes the model using **pickle**  
- Wraps it in a **Flask web app**  
- Deploys it on **Render Cloud** with **Gunicorn**

---

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?logo=python" />
  <img src="https://img.shields.io/badge/Framework-Flask-black?logo=flask" />
  <img src="https://img.shields.io/badge/Model-Logistic%20Regression-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Deployed%20On-Render-0466C8?logo=render" />
</p>

<p align="center">
  <a href="https://github.com/Pinkkygold">
    <img src="https://img.shields.io/badge/GitHub-Pinkkygold-181717?logo=github" />
  </a>
  <a href="https://www.linkedin.com/in/awab-abdalla">
    <img src="https://img.shields.io/badge/LinkedIn-Awab%20Abdalla-0A66C2?logo=linkedin" />
  </a>
</p>

---

## 🧠 Projects in This Folder

### 🎗️ 1. Simple Breast Cancer Predictor

> Predicts whether a breast tumor is **benign** or **malignant** based on a single feature: **mean radius**.

- **Model**: Logistic Regression (`scikit-learn`)
- **Input**: Mean radius (numeric)
- **Output**:  
  - `0` → ✅ Benign  
  - `1` → ⚠️ Malignant  
  - Plus prediction probability

**Live Demo:**  
👉 https://simple-breast-cancer-predictor.onrender.com  

**GitHub Project:**  
👉 https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Supervised%20learning/LogisticRegression/Breast%20Cancer  

This project demonstrates:
- Data preprocessing & model training  
- Model saving with `pickle`  
- A clean HTML/CSS interface  
- Deployment on Render with `gunicorn app:app`  

---

### ❤️ 2. Simple Heart Attack Predictor

> Predicts the **risk of heart attack** based solely on a person’s **age**.

- **Model**: Logistic Regression (`scikit-learn`)
- **Input**: Age (numeric)
- **Output**:  
  - `0` → ✅ Low risk  
  - `1` → ⚠️ High risk  
  - With probability (confidence score)

**Live Demo:**  
👉 https://machine-learning-projects-s5t4.onrender.com  

**GitHub Project:**  
👉 https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Supervised%20learning/LogisticRegression/Heartattack%20prediction  

This project showcases:
- Full ML pipeline with a very simple feature  
- Intuitive UI for real-time inference  
- Production-style deployment using Gunicorn & Render  

---

## 🧩 Shared Tech Stack

All projects in this folder use:

- **Python**
- **Flask** – Web framework
- **scikit-learn** – Logistic Regression
- **NumPy, pandas** – Data processing
- **HTML5, CSS3** – Frontend
- **Render** – Cloud deployment
- **Gunicorn** – WSGI server
- **pickle** – Model serialization

---

## 🗂️ Recommended Folder Structure

```bash
LogisticRegression/
│
├── Breast Cancer/
│   ├── app.py
│   ├── BreastCancer.pkl
│   ├── requirements.txt
│   ├── Procfile
│   ├── static/
│   └── templates/
│
└── Heartattack prediction/
    ├── app.py
    ├── Heartattack.pkl
    ├── requirements.txt
    ├── Procfile
    ├── static/
    └── templates/
````

Each subfolder contains its own **README**, app code, model, and deployment files.

---

## 🎯 Learning Outcomes

By exploring the projects in this folder, you can learn how to:

* Build **Logistic Regression** models for binary classification
* Export models with `pickle` for reuse in applications
* Integrate ML models into **Flask** web apps
* Deploy real ML applications on **Render**
* Design minimal yet intuitive ML UI interfaces

---

## 👨‍💻 Author

**Awab Elkhair Abdalla**
📍 Machine Learning Engineer · Researcher · Volunteer

* 💼 GitHub: [Pinkkygold](https://github.com/Pinkkygold)
* 🌐 LinkedIn: [awab-abdalla](https://www.linkedin.com/in/awab-abdalla)
* ✉️ Email: **[awab1355@gmail.com](mailto:awab1355@gmail.com)**

> “Turning simple models into real, accessible tools that help people understand AI.”

---

## ⭐ Support

If you find these projects useful or inspiring:

* ⭐ Star the repository on GitHub
* 🍴 Fork it to build your own versions
* 💬 Share feedback or ideas for new mini-apps

Your support helps keep more **open-source ML apps** coming! 🚀

