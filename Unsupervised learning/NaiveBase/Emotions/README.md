

# 🎭 **Emotion Detection Web App**

### *Analyze text emotions instantly using Machine Learning & Flask*

<p align="center">
  <a href="https://emotions-predictor.onrender.com">
    <img src="https://img.shields.io/badge/Live%20Demo-Render-blue?style=for-the-badge" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Flask-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-ScikitLearn-green?style=for-the-badge" />
</p>

<p align="center">
A simple, elegant, and interactive web app that predicts emotions from text using a trained Machine Learning model.
</p>

---

## 🚀 **Live Demo**

🔗 **[https://emotions-predictor.onrender.com](https://emotions-predictor.onrender.com)**

---

## 📌 **Overview**

This project is a fast, lightweight **ML-powered Emotion Classification Web App** built using:

* **Scikit-Learn** (ML Pipeline)
* **TF-IDF Vectorization**
* **SMOTE** (for class balancing)
* **Flask + Gunicorn** (backend + deployment)
* **Render Cloud** (hosting)

It accepts **any text** and returns:

* 🎭 **Top emotion**
* 📊 **Probability chart** for all emotion classes
* ⚡ Quick test buttons for “Joy”, “Sadness”, “Anger”

Perfect for your **portfolio**, **ML showcase**, **resume link**, or **university applications**.

---

## 🖥️ **Screenshot Preview**


<p align="center">
  <img width="1394" height="801" alt="Screenshot 2025-11-22 at 5 12 31 PM" src="https://github.com/user-attachments/assets/ffc4ffc9-4b44-457b-b6db-6fc9c4aa5392" />

</p>

---

## 🧠 **Model Architecture**

* **Pipeline:**

  * `TfidfVectorizer(stop_words='english')`
  * `SMOTE()` (imbalanced-learn)
  * **Classifier:** Multinomial Naive Bayes / Logistic Regression
* **Training Notebook:** `.ipynb` (not included in deployment)
* **Saved Model:** `Emotions_model.pkl` using `pickle`

### Exported using:

```python
with open("Emotions_model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

## 📁 **Project Structure**

```txt
.
├── app.py
├── Emotions_model.pkl
├── requirements.txt
└── templates/
    └── index.html
```

* `app.py` – Flask backend
* `index.html` – Responsive UI
* `Emotions_model.pkl` – ML model
* `requirements.txt` – Dependencies

---

## ▶️ **Run Locally**

### 1️⃣ Clone the project

```bash
git clone https://github.com/<YOUR-USERNAME>/<REPO-NAME>.git
cd <REPO-NAME>
```

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
# .venv\Scripts\activate    # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 🌐 **Deploying on Render**

This app is already deployed at:

### 👉 [https://emotions-predictor.onrender.com](https://emotions-predictor.onrender.com)

To redeploy:

1. Commit your files to GitHub
2. Go to **Render → New → Web Service**
3. Choose your repo
4. Set:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

Render will automatically build & deploy.

---

## 🔌 **REST API Endpoint**

### **POST** `/api/predict`

#### Request:

```json
{
  "text": "I feel amazing today!"
}
```

#### Response:

```json
{
  "prediction": "joy",
  "probabilities": [
    {"label": "joy", "prob": 86.52},
    {"label": "neutral", "prob": 9.12},
    {"label": "sadness", "prob": 1.67},
    {"label": "anger", "prob": 0.88}
  ]
}
```

---

## 🛠️ **Tech Stack**

| Layer        | Technology            |
| ------------ | --------------------- |
| ML Model     | Scikit-Learn Pipeline |
| Vectorizer   | TF-IDF                |
| Oversampling | SMOTE                 |
| Backend      | Flask                 |
| Server       | Gunicorn              |
| Deployment   | Render                |
| Frontend     | HTML + Jinja2         |

---

## ⭐ **Future Enhancements**

* 🌍 Multilingual emotion detection (Arabic, Turkish, English)
* 🤖 Upgrade to **BERT / Transformers**
* 📊 Add more Plotly visualizations
* 🔥 Add sentiment polarity scoring
* 📝 Add user history dashboard

---

## 💙 **Author**

**Awab Elkhair Abdalla Idris**
Machine Learning Engineer | AI enthusiast | UN Youth Delegate

🔗 GitHub: (https://github.com/Pinkkygold)
🔗 LinkedIn: www.linkedin.com/in/awab-abdalla


