
# 💸 Restaurant Tip Prediction Web App (KNN + Flask)

This project is a Machine Learning–powered web application that predicts the expected **tip amount** for a restaurant bill using a **K-Nearest Neighbors (KNN) regression model**.
Users provide basic table info (bill, day, time, party size), and the model estimates the tip and visualizes it interactively.

🔗 **Live Demo:** [https://tipsamount.onrender.com](https://tipsamount.onrender.com)

---

<p align="center">
  <a href="https://tipsamount.onrender.com">
    <img src="https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=render" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Framework-Flask-black?style=for-the-badge&logo=flask" />
  <img src="https://img.shields.io/badge/Model-KNN%20Regressor-green?style=for-the-badge&logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=for-the-badge&logo=render" />
</p>

---

## 🖼️ Screenshot


<p align="center">
 <img width="1334" height="794" alt="AppScreenshot" src="https://github.com/user-attachments/assets/8efcbd3f-2c50-4393-a220-ad2a3996dd20" />

</p>

---

## 🚀 Features

* Predicts **tip amount** based on bill details
* Computes **tip percentage**
* Interactive **Plotly bar chart** (Total Bill vs Predicted Tip)
* Clean dark UI with example presets
* Model trained using **KNN** (best *k* selected via cross-validation)
* Fully deployed and accessible on Render

---

## 🧠 Machine Learning Model

The app uses a **KNN Regressor** trained on the classical Seaborn `tips` dataset.

### Training includes:

* Data cleaning
* One-hot encoding of categorical features
* Scaling numerical columns
* KNN hyperparameter tuning
* Exporting the model as `.pkl`:

```python
import pickle
with open("tips_knn_model.pkl", "wb") as f:
    pickle.dump(model, f)
```

---

## 📊 Input Features

The model expects:

* **total_bill**
* **sex** (Male/Female)
* **smoker** (Yes/No)
* **day** (Thur/Fri/Sat/Sun)
* **time** (Lunch/Dinner)
* **size** (number of customers)

It outputs:

* Predicted **tip (amount)**
* **Tip percentage** relative to total bill
* Plotly visualization

---

## 🎨 Plotly Visualization

The app includes a dynamic Plotly bar chart comparing:

* User’s total bill
* Model’s predicted tip

Insightful, clean, and interactive — great for UI engagement.

---

## 📁 Project Structure

```text
Tips/
├── app.py
├── tips_knn_model.pkl
├── requirements.txt
└── templates/
    └── index.html
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/Pinkkygold/Machine-Learning-projects
cd "Machine-Learning-projects/Unsupervised learning/K-nearest neighbors/Tips"

python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

pip install -r requirements.txt
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment Instructions (Render)

This app is live at:

🔗 [https://tipsamount.onrender.com](https://tipsamount.onrender.com)

To deploy:

1. Push project to GitHub
2. Go to Render → New Web Service
3. Connect repo
4. Set:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
gunicorn app:app
```

Render automatically deploys the service.

---

## 🛠️ Tech Stack

* Python 3.x
* Flask
* Scikit-Learn
* Pandas / NumPy / SciPy
* Plotly.js
* Gunicorn
* Render Cloud

---

## ⚠️ Disclaimer

This app is for educational and demo purposes only.
Not indicative of real-world restaurant tipping policies.

---

## ✨ Author

Created by **Awab Elkhair Abdalla Idris (Pinkkygold)**
Machine Learning Engineer (in progress) | AI for Social Impact | UN Youth Delegate

* GitHub: [https://github.com/Pinkkygold](https://github.com/Pinkkygold)
* LinkedIn: www.linkedin.com/in/awab-abdalla


If you like the project, ⭐ star the repo!

---
