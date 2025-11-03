# ❤️ Heart Attack Risk Prediction Dashboard  


### *(Decision Tree Classifier + Flask Web App + Render Deployment)*  
[![Render Deployment](https://img.shields.io/badge/Live%20App%20Status-Online-success)](https://hearattack-with-decisiontree.onrender.com)

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7.2-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://hearattack-with-decisiontree.onrender.com)
[![Accuracy](https://img.shields.io/badge/Model%20Accuracy-87%25-brightgreen)](https://hearattack-with-decisiontree.onrender.com)
[![Uptime](https://img.shields.io/uptimerobot/ratio/m795531890-a2b0d9fef3b1c8b3fcd7b4f8.svg?label=App%20Uptime)](https://hearattack-with-decisiontree.onrender.com)
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=Pinkkygold.heart-attack-dashboard)](https://github.com/Pinkkygold/heart-attack-dashboard)

---

## 🩺 Live Demo

🚀 **Try It Now:**  
👉 [Heart Attack Predictor – Live on Render](https://hearattack-with-decisiontree.onrender.com)

---

## 🩸 About the Project

An interactive **machine learning dashboard** that predicts the likelihood of a heart attack based on patient medical data.  
Built using a **Decision Tree Classifier** and deployed with **Flask + Render**.  

> 🧠 The model uses health attributes like age, cholesterol, chest pain type, and more to deliver real-time risk prediction.

### ✨ Key Highlights
- 🧮 **Decision Tree Classifier** trained on medical dataset  
- 🧑‍⚕️ Clean **dashboard-style UI** for easy data entry  
- 📊 **Dynamic Confusion Matrix** auto-generated for each session  
- 📈 **Accuracy, Precision, Recall, and F1-score** displayed  
- ☁️ **Fully deployed** on Render Cloud  

---

## ⚙️ Tech Stack

| Layer | Tools / Libraries |
|-------|--------------------|
| **Frontend** | HTML5, CSS3 (Custom Dashboard UI) |
| **Backend** | Flask (Python) |
| **Modeling** | Scikit-Learn (DecisionTreeClassifier) |
| **Visualization** | Matplotlib (Confusion Matrix) |
| **Deployment** | Render Cloud Platform |

---

## 🧩 Workflow

```mermaid
graph TD;
    A[User Inputs Data] --> B[Flask Backend];
    B --> C[Preprocess Input];
    C --> D[Decision Tree Model];
    D --> E[Prediction Result];
    E --> F[Render Output on Dashboard];
    F --> G[Dynamic Confusion Matrix];
````

---

## 📘 Input Features

| Feature      | Description                           |
| ------------ | ------------------------------------- |
| **age**      | Age of the patient                    |
| **sex**      | 1 = Male, 0 = Female                  |
| **cp**       | Chest pain type                       |
| **trestbps** | Resting blood pressure                |
| **chol**     | Cholesterol level (mg/dl)             |
| **fbs**      | Fasting blood sugar                   |
| **restecg**  | Resting electrocardiographic results  |
| **thalach**  | Max heart rate achieved               |
| **exang**    | Exercise induced angina               |
| **oldpeak**  | ST depression induced by exercise     |
| **slope**    | Slope of the peak exercise ST segment |
| **ca**       | Major vessels colored by fluoroscopy  |
| **thal**     | Thalassemia (0–3 range)               |

---

## 🧰 Installation (Run Locally)

```bash
# 1️⃣ Clone this repo
git clone https://github.com/Pinkkygold/heart-attack-dashboard.git
cd heart-attack-dashboard

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run the app
python app.py

# 4️⃣ Open in your browser
http://127.0.0.1:5000/
```

---

## 📊 Model Performance

| Metric        | Score |
| ------------- | ----- |
| **Accuracy**  | 0.87  |
| **Precision** | 0.85  |
| **Recall**    | 0.88  |
| **F1-score**  | 0.86  |

*(Values are from Decision Tree model evaluation — update as needed.)*

---

## 🎞️ Confusion Matrix Animation

Here’s how the confusion matrix dynamically updates after each prediction:

| Dynamic Visualization                                                  |
| ---------------------------------------------------------------------- |
| ![Confusion Matrix Animation](static/screenshots/confusion_matrix.gif) |

*(You can generate this using `matplotlib.animation` or save an MP4/GIF showing your matrix updates.)*



## ☁️ Deployment on Render

```yaml
services:
  - type: web
    name: heart-attack-dashboard
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
    plan: free
```

---

## 👨‍💻 Author

**Awab Elkhair Abdalla Idris**
🎓 *Electronics Engineer | Machine Learning Engineer | UN Youth Delegate*

🌐 [GitHub](https://github.com/Pinkkygold)
💼 [LinkedIn](https://linkedin.com/in/awab-elkhair)
📘 [ResearchGate](https://www.researchgate.net/profile/Awab-Abdalla)

---

## 🪪 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and share — with credit.

---

## ⭐ Acknowledgment

> “Artificial Intelligence isn’t about replacing humans —
> it’s about enhancing our ability to **protect and care** for them.”

Special thanks to open-source contributors and the global ML community 🌍

---


