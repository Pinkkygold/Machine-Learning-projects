
# ❤️ Simple Heart Attack Predictor

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.5.0-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://machine-learning-projects-s5t4.onrender.com)

> A clean, interactive **machine learning web app** that predicts the likelihood of a **heart attack** based solely on a person’s **age**.  
> Built with *Flask* and *Logistic Regression*, deployed on **Render Cloud**.

🔗 **Live Demo:**  
👉 [https://machine-learning-projects-s5t4.onrender.com](https://machine-learning-projects-s5t4.onrender.com)

---

## 🧠 Overview

This project demonstrates a full **end-to-end ML workflow** — from model training to deployment.  
It uses a simple logistic regression model to predict heart attack risk and provides a minimalist, user-friendly interface for real-time predictions.

### 💡 Key Highlights
- Clean Flask web app interface  
- Predicts heart attack risk from **age**  
- Probability-based output with confidence level  
- Fully deployed on **Render Cloud** using **Gunicorn**

---

## 🧩 Tech Stack

| Layer | Technology |
|:------|:------------|
| **Frontend** | HTML5, CSS3 (responsive, modern) |
| **Backend** | Flask (Python web framework) |
| **Model** | Logistic Regression (`scikit-learn`) |
| **Data Processing** | NumPy, pandas |
| **Deployment** | Render + Gunicorn |

---

## 🖼️ Screenshot Preview

Below is an example of the live web interface.  

<p align="center">
  <img src="static/preview.png" alt="App Screenshot" width="80%">
</p>


---

## ⚙️ Local Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Pinkkygold/simple-heartattack-predictor.git
cd simple-heartattack-predictor
````

### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App Locally

```bash
python app.py
```

or (for production-style run)

```bash
gunicorn app:app --bind 0.0.0.0:5000
```

Then visit ➜ [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧮 Project Structure

```
simple-heartattack-predictor/
│
├── app.py                 # Flask web app
├── Heartattack.pkl        # Trained logistic regression model
├── requirements.txt       # Python dependencies
├── Procfile               # For Render deployment
│
├── static/
│   ├── style.css          # Frontend styling
│   └── preview.png        # Screenshot preview (optional)
│
└── templates/
    └── index.html         # HTML interface
```

---

## 💡 Model Details

* **Algorithm:** Logistic Regression
* **Feature:** `Age`
* **Output:** Binary prediction

  * `1` → High risk ⚠️
  * `0` → Low risk ✅
* **Probability Output:** Derived from the logistic sigmoid function

---

## 🚀 Deployment on Render

1. Push the project to GitHub
2. Connect your repository to **Render**
3. Create a new *Web Service*
4. Set the **Start Command** to:

   ```
   gunicorn app:app
   ```
5. Deploy and share your live link 🌍

---

## 🧑‍💻 Author

**Awab Elkhair**
📍 *Machine Learning Engineer · Researcher · Volunteer*
🌐 [ResearchGate](https://www.researchgate.net/profile/Awab-Abdalla)
💼 [GitHub: Pinkkygold](https://github.com/Pinkkygold)
📫 *“Building AI that empowers people, not replaces them.”*

---

## 🪶 License

This project is released under the **MIT License**.
You’re free to fork, use, and modify it for learning, projects, or inspiration.

---

### ⭐ If this project inspired you,

Please **star** the repo — it helps more learners discover it and motivates me to share more open-source ML apps! 🌟


---

