# 🚗 Car Price Prediction

### *(Flask + Scikit-Learn + Render Cloud Deployment)*

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.7.2-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.3.3-darkblue?logo=pandas)](https://pandas.pydata.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://car-price-predictor-6t6e.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

---

## 📘 Overview

**Car Price Prediction** is a **Machine Learning web application** that predicts car prices based on various specifications like brand, engine size, horsepower, and other technical features. The app integrates a **Linear Regression model** trained on comprehensive automotive data, powered by **Flask**, and deployed on **Render Cloud**.

> 🎯 **Live Demo:** [https://car-price-predictor-6t6e.onrender.com](https://car-price-predictor-6t6e.onrender.com)

---

## 🚀 Key Features

✅ **Interactive Price Prediction** - User-friendly form for car specifications  
✅ **Real-time Predictions** - Instant price estimates using trained ML model  
✅ **Data Analysis Dashboard** - Visualizations and brand analysis  
✅ **Brand Categorization** - Automatically categorizes brands as Budget, Mid-Range, or Luxury  
✅ **Responsive Web Design** - Bootstrap-powered UI that works on all devices  
✅ **REST API Endpoints** - Programmatic access to predictions  
✅ **Cloud Deployment** - Fully deployed on **Render Cloud**

---

## 🧠 Machine Learning Model

* **Algorithm:** Linear Regression
* **Dataset:** Car Price Assignment Dataset (205 records, 26 features)
* **Target Variable:** `price` (Car price in USD)

### Key Features Used for Prediction:

| Feature | Description |
|---------|-------------|
| **Brand** | Car manufacturer (23 unique brands) |
| **Engine Size** | Engine displacement in cubic centimeters |
| **Horsepower** | Engine power output |
| **Curb Weight** | Vehicle weight without occupants |
| **Fuel Type** | Gas or Diesel |
| **Car Body** | Sedan, Convertible, Hatchback, etc. |
| **Drive Wheel** | FWD, RWD, 4WD |
| **MPG** | City and Highway fuel efficiency |
| **Dimensions** | Wheelbase, Length, Width, Height |
| **Technical Specs** | Bore Ratio, Stroke, Compression Ratio |

---

## 📊 Model Performance

The model was trained and evaluated using **Scikit-Learn** with 80-20 train-test split:

| Metric | Value |
|--------|-------|
| **R² Score** | ~85-90% |
| **Mean Squared Error (MSE)** | ~7,000,000 |
| **Root Mean Squared Error (RMSE)** | ~$2,700 |
| **Average Prediction Error** | ±$2,700 |

> The model shows strong predictive power for car prices based on technical specifications and brand factors. Performance may vary based on feature combinations.

---

## 🧩 Project Structure

```
Car Price predictor/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── runtime.txt                     # Python version specification
├── Procfile                        # Render deployment configuration
├── wsgi.py                         # WSGI entry point
├── CarPrice_Assignment.csv         # Original dataset
├── Car_price_model.pkl            # Trained ML model (auto-generated)
├── feature_columns.pkl            # Feature columns mapping (auto-generated)
├── templates/
│   ├── index.html                 # Home page with overview
│   ├── predict.html               # Price prediction form
│   └── result.html                # Data analysis dashboard
├── static/
│   └── style.css                  # Custom CSS styling
└── README.md                      # Project documentation
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git
cd "Machine-Learning-projects/Regression models/Car Price predictor"
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

## 🎯 Usage Guide

### 🔮 Price Prediction
1. Navigate to **[/predict](https://car-price-predictor-6t6e.onrender.com/predict)** endpoint
2. Fill in car specifications:
   - Select brand and body type
   - Enter technical specifications (engine size, horsepower, etc.)
   - Input dimensions and performance metrics
3. Click **"Predict Car Price"** for instant estimation

### 📊 Data Analysis
1. Visit **[/analyze](https://car-price-predictor-6t6e.onrender.com/analyze)** endpoint
2. Explore:
   - Brand distribution charts
   - Price distribution analysis
   - Feature correlation heatmaps
   - Dataset statistics

### 🌐 API Access
**Endpoint:** `POST /api/predict`

**Example Usage:**
```python
import requests

data = {
    'Brand': 'toyota',
    'enginesize': 120,
    'horsepower': 100,
    'curbweight': 2500,
    'fueltype': 'gas',
    'carbody': 'sedan'
}

response = requests.post('https://car-price-predictor-6t6e.onrender.com/api/predict', json=data)
prediction = response.json()
```

---

## 🚀 Deployment on Render

### Build Command:
```bash
pip install -r requirements.txt
```

### Start Command:
```bash
gunicorn app:app
```

### Environment:
- **Python Version:** 3.9+
- **Port:** `$PORT` (automatically provided by Render)

### Deployment Status:
✅ **Successfully Deployed**  
🔗 **Live URL:** [https://car-price-predictor-6t6e.onrender.com](https://car-price-predictor-6t6e.onrender.com)

---

## 🛠️ Tech Stack

* **Backend Framework:** Flask 3.1.2
* **Machine Learning:** Scikit-Learn 1.7.2
* **Data Processing:** Pandas 2.3.3, NumPy 2.3.4
* **Visualization:** Matplotlib, Seaborn
* **Frontend:** HTML5, CSS3, Bootstrap 5
* **Deployment:** Render, Gunicorn
* **Model Serialization:** Joblib

---

## 📈 Features Analysis

### Brand Categories:
- **Budget:** < $10,000 (Chevrolet, Dodge, Honda, etc.)
- **Mid-Range:** $10,000 - $20,000 (Toyota, Volkswagen, Audi, etc.)
- **Luxury:** > $20,000 (BMW, Jaguar, Porsche, Buick, etc.)

### Key Insights:
- Engine size and horsepower show strong positive correlation with price
- Luxury brands command significant price premiums
- Car body type significantly impacts pricing
- Fuel efficiency shows inverse relationship with price

---

## 🔮 Future Enhancements

- [ ] Implement multiple ML algorithms (Random Forest, XGBoost)
- [ ] Add feature importance visualization
- [ ] Include confidence intervals for predictions
- [ ] Add user authentication and prediction history
- [ ] Implement advanced filtering and comparison tools
- [ ] Add more detailed brand performance analytics

---

## 👨‍💻 Author

**Awab Elkhair Abdalla**  
🎓 *AI & Machine Learning Enthusiast*  
🌍 *Building intelligent systems that solve real-world problems.*

🔗 [LinkedIn](www.linkedin.com/in/awab-abdalla)  
📎 [ResearchGate](https://www.researchgate.net/profile/Awab-Abdalla)  
💻 [GitHub](https://github.com/Pinkkygold)

---

## 🧾 License

This project is open-sourced under the **MIT License**.  
The car dataset is used for **educational and demonstration purposes** to showcase machine learning application development.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check [issues page](https://github.com/Pinkkygold/Machine-Learning-projects/issues) if you want to contribute.

---

<div align="center">

### 🚗 *Drive Your Decisions with Data* 🚗

**Live Application:** [https://car-price-predictor-6t6e.onrender.com](https://car-price-predictor-6t6e.onrender.com)

</div>
