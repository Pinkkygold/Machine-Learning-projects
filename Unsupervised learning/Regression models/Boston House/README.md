

# 🏠 Boston House Price Prediction

### *(Flask + Scikit-Learn + Render Cloud Deployment)*

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://house-price-prediction-d58i.onrender.com/predict)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

---

## 📘 Overview

**Boston House Price Prediction** is a **Machine Learning web app** that predicts the median house prices in Boston using socioeconomic and environmental factors.
The app integrates a **Linear Regression model** trained on the **Boston Housing Dataset**, powered by **Flask**, and deployed seamlessly on **Render Cloud**.

> 🎯 **Live Demo:** [house-price-prediction-d58i.onrender.com](https://house-price-prediction-d58i.onrender.com/predict)

---

## 🚀 Key Features

✅ Interactive and responsive web UI (Flask + HTML/CSS)
✅ Real-time price predictions via REST API (`/api/predict`)
✅ Fully deployed on **Render Cloud**
✅ Includes local testing via `test_model.py`
✅ Clean model serialization and loading with `pickle`

---

## 🧠 Machine Learning Model

* **Algorithm:** Linear Regression
* **Dataset:** [Boston Housing Dataset (Kaggle)](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices)
* **Target Variable:** `MEDV` (Median value of owner-occupied homes in $1000’s)

| Feature     | Description                                                                                                                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CRIM**    | Per capita crime rate by town                                                                                                                                                                        |
| **ZN**      | Proportion of residential land zoned for lots over 25,000 sq.ft                                                                                                                                      |
| **INDUS**   | Proportion of non-retail business acres per town                                                                                                                                                     |
| **CHAS**    | Charles River dummy variable (1 if tract bounds river, 0 otherwise)                                                                                                                                  |
| **NOX**     | Nitric oxide concentration (parts per 10 million)                                                                                                                                                    |
| **RM**      | Average number of rooms per dwelling                                                                                                                                                                 |
| **AGE**     | Proportion of owner-occupied units built before 1940                                                                                                                                                 |
| **DIS**     | Weighted distances to five Boston employment centers                                                                                                                                                 |
| **RAD**     | Index of accessibility to radial highways                                                                                                                                                            |
| **TAX**     | Full-value property tax rate per $10,000                                                                                                                                                             |
| **PTRATIO** | Pupil–teacher ratio by town                                                                                                                                                                          |
| **B**       | *Number of Black residents in the town.* ⚠️ *Note: This is not a racially motivated metric; it originates from historical versions of the dataset and is included solely for research completeness.* |
| **LSTAT**   | Percentage of lower-status population                                                                                                                                                                |
| **MEDV**    | Median value of owner-occupied homes in $1000s *(Target variable)*                                                                                                                                   |

---

## 📊 Model Performance

The model was trained and evaluated using **Scikit-Learn** metrics:

| Metric                             | Value |
| :--------------------------------- | :---- |
| **R² Score (Train)**               | 0.74  |
| **R² Score (Test)**                | 0.68  |
| **Mean Squared Error (MSE)**       | 24.8  |
| **Root Mean Squared Error (RMSE)** | 4.98  |

> The results indicate a solid baseline performance for a simple Linear Regression model on this dataset.
> Future improvements could include feature scaling, regularization (Ridge/Lasso), and ensemble methods.

*(You can optionally visualize performance in Jupyter using `matplotlib` or `seaborn`.)*

---

## 🧩 Project Structure

```
BostonHousePricePrediction/
│
├── app.py                        # Main Flask application
├── Boston_regression_model.pkl    # Trained ML model
├── HousingData.csv                # Dataset used for training
├── templates/
│   ├── index.html                 # Input form
│   └── result.html                # Output page
├── static/
│   └── style.css                  # Custom styling
├── test_model.py                  # Local test script
├── requirements.txt               # Dependencies
└── README.md                      # Documentation
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/BostonHousePricePrediction.git
cd BostonHousePricePrediction
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App

```bash
python app.py
```

Visit 👉 [http://127.0.0.1:5001/](http://127.0.0.1:5001/)

---

## 🧪 Testing the Model

Run:

```bash
python test_model.py
```

Expected output:

```
✅ Model loaded successfully!
✅ Test prediction: 17.75
```

---

## 🌐 Deployment on Render

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
gunicorn app:app
```

**Environment:** Python 3.10+
**Port:** `$PORT` *(automatically provided by Render)*

🔗 **Live App:** [https://house-price-prediction-d58i.onrender.com/predict](https://house-price-prediction-d58i.onrender.com/predict)

---

## 🔍 API Usage

**Endpoint:** `POST /api/predict`

**Example Request:**

```json
{
  "CRIM": 0.1,
  "ZN": 25.0,
  "INDUS": 5.0,
  "CHAS": 0,
  "NOX": 0.5,
  "RM": 6.0,
  "AGE": 30.0,
  "DIS": 5.0,
  "RAD": 2.0,
  "TAX": 300.0,
  "PTRATIO": 16.0,
  "B": 390.0,
  "LSTAT": 5.0
}
```

**Example Response:**

```json
{
  "predicted_medv": 18.2,
  "predicted_price_usd": 18200.0,
  "status": "success"
}
```

---

## 🛠️ Tech Stack

* 🐍 **Python 3.13**
* 🌐 **Flask**
* 📈 **Scikit-Learn**
* 📊 **Pandas / NumPy**
* 🔧 **Gunicorn**
* ☁️ **Render Cloud Hosting**

---

## 👨‍💻 Author

**Awab Elkhair Abdalla**
🎓 *AI & Machine Learning Enthusiast*
🌍 *Building intelligent systems that make life simpler.*

🔗 [LinkedIn](www.linkedin.com/in/awab-abdalla)
📎 [ResearchGate](https://www.researchgate.net/profile/Awab-Abdalla)
💻 [GitHub](https://github.com/Pinkkygold)

---

## 🧾 License

This project is open-sourced under the **MIT License**.
The dataset originates from legacy academic research and is included **for educational and historical purposes only**.

---

