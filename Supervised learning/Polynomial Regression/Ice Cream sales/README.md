# 🍦 Ice Cream Sales Prediction

### *(Flask + Scikit-Learn + Polynomial Regression + Render Cloud Deployment)*

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-black?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3.0-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0.3-darkblue?logo=pandas)](https://pandas.pydata.org/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://ice-cream-sales-jv5w.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)](LICENSE)

---

## 📘 Overview

**Ice Cream Sales Prediction** is a **Machine Learning web application** that forecasts ice cream sales based on temperature using **Polynomial Regression**. The app captures the non-linear relationship between temperature and sales, providing accurate predictions with interactive visualizations. Built with **Flask**, powered by **Scikit-Learn**, and deployed on **Render Cloud**.

> 🎯 **Live Demo:** [https://ice-cream-sales-jv5w.onrender.com](https://ice-cream-sales-jv5w.onrender.com)

---

## 🚀 Key Features

✅ **Interactive Polynomial Regression** - Multiple degrees (2-5) for optimal modeling  
✅ **Real-time Sales Predictions** - Instant sales estimates at any temperature  
✅ **Dynamic Visualizations** - Interactive charts with prediction markers  
✅ **Model Performance Metrics** - R² scores and MSE for each polynomial degree  
✅ **Responsive Dashboard** - Professional UI that works on all devices  
✅ **REST API Endpoints** - Programmatic access to predictions and data  
✅ **Cloud Deployment** - Fully deployed on **Render Cloud**

---

## 🧠 Machine Learning Model

* **Algorithm:** Polynomial Regression with Linear Regression
* **Dataset:** 49 data points of temperature vs. ice cream sales
* **Target Variable:** `Ice Cream Sales (units)`

### Model Configuration:

| Feature | Description |
|---------|-------------|
| **Polynomial Degrees** | 2, 3, 4, 5 (user-selectable) |
| **Training Split** | 80% training, 20% testing |
| **Random State** | 42 for reproducible results |
| **Features** | Temperature (°C) polynomial transformations |

---

## 📊 Model Performance

The polynomial regression model was trained and evaluated with different degrees:

| Polynomial Degree | R² Score | MSE | Best For |
|-------------------|----------|-----|----------|
| **Degree 2** | ~84.3% | ~14.88 | **Optimal Balance** |
| **Degree 3** | Varies | Varies | Complex patterns |
| **Degree 4** | Varies | Varies | High flexibility |
| **Degree 5** | Varies | Varies | Maximum complexity |

> **Degree 2 (Quadratic)** provides the best balance of performance and generalization for this dataset.

---

## 🧩 Project Structure

```
polynomial regression/
└── Ice Cream sales/
    │
    ├── app.py                          # Main Flask application
    ├── wsgi.py                         # WSGI entry point for deployment
    ├── requirements.txt                # Python dependencies
    ├── runtime.txt                     # Python 3.11.4 specification
    ├── Ice_cream_selling_data.csv      # Dataset (49 records)
    │
    ├── templates/
    │   └── index.html                  # Interactive dashboard
    │
    └── static/
        └── style.css                   # Professional styling
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git
cd "Machine-Learning-projects/polynomial regression/Ice Cream sales"
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

### 4️⃣ Run the Flask Application

```bash
python app.py
```

Visit 👉 [http://localhost:5000](http://localhost:5000)

---

## 🎯 Usage Guide

### 🔮 Sales Prediction
1. **Navigate** to the main application
2. **Select Polynomial Degree** (2-5) for model complexity
3. **Enter Temperature** in Celsius for prediction
4. **Click Predict** for instant sales estimation
5. **View Results** with visual markers on the chart

### 📊 Data Analysis
- **Scatter Plot**: Actual sales data points
- **Regression Curve**: Polynomial fit visualization  
- **Performance Metrics**: R² score and MSE for model evaluation
- **Statistics**: Dataset overview and correlations

### 🌐 API Endpoints

**Price Prediction:**
```python
import requests

data = {
    'temperature': 25.5,
    'degree': 2
}

response = requests.post('https://ice-cream-sales-jv5w.onrender.com/predict', json=data)
prediction = response.json()
```

**Data Access:**
- `GET /api/data` - Raw dataset
- `GET /api/stats` - Statistical summary
- `GET /health` - Service status

---

## 🚀 Deployment on Render

### Build Command:
```bash
pip install -r requirements.txt
```

### Start Command:
```bash
gunicorn wsgi:app
```

### Environment:
- **Python Version:** 3.11.4
- **Port:** `$PORT` (automatically provided by Render)

### Deployment Status:
✅ **Successfully Deployed**  
🔗 **Live URL:** [https://ice-cream-sales-jv5w.onrender.com](https://ice-cream-sales-jv5w.onrender.com)

---

## 🛠️ Tech Stack

* **Backend Framework:** Flask 2.3.3
* **Machine Learning:** Scikit-Learn 1.3.0
* **Data Processing:** Pandas 2.0.3, NumPy 1.24.3
* **Visualization:** Matplotlib 3.7.2, Seaborn 0.12.2
* **Frontend:** HTML5, CSS3, JavaScript
* **Deployment:** Render, Gunicorn 21.2.0
* **Model Training:** Polynomial Features, Linear Regression

---

## 📈 Business Insights

### Temperature Impact:
- **Below 0°C**: Low sales (0-20 units)
- **0°C to 10°C**: Moderate sales (5-40 units)  
- **Above 10°C**: High sales potential (40+ units)
- **Optimal Range**: 15°C-25°C for maximum sales

### Key Findings:
- **Strong positive correlation** between temperature and sales
- **Non-linear relationship** best captured by polynomial regression
- **Seasonal patterns** evident in sales data
- **Prediction accuracy** suitable for inventory planning

---

## 🔮 Future Enhancements

- [ ] Add time-series analysis for seasonal trends
- [ ] Implement multiple regression algorithms comparison
- [ ] Include weather forecast integration
- [ ] Add inventory optimization recommendations
- [ ] Implement user accounts for saved predictions
- [ ] Add export functionality for business reports
- [ ] Include confidence intervals for predictions

---

## 👨‍💻 Author

**Pinkkygold**  
🎓 *AI & Machine Learning Enthusiast*  
🌍 *Building practical ML applications for real-world problems.*

💻 [GitHub](https://github.com/Pinkkygold)  
🔗 [Machine Learning Projects](https://github.com/Pinkkygold/Machine-Learning-projects)

---

## 🧾 License

This project is open-sourced under the **MIT License**.  
The ice cream sales dataset is used for **educational and demonstration purposes** to showcase polynomial regression applications.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check [issues page](https://github.com/Pinkkygold/Machine-Learning-projects/issues) if you want to contribute.

---

<div align="center">

### 🍦 *Sweet Predictions with Polynomial Intelligence* 🍦

**Live Application:** [https://ice-cream-sales-jv5w.onrender.com](https://ice-cream-sales-jv5w.onrender.com)

*"Predicting sweetness, one degree at a time!"*

</div>

---

## 📊 Example Prediction

**Scenario:** Summer day at 25°C  
**Predicted Sales:** ~45-50 units  
**Model Confidence:** High (R² = 84.3%)

**Use Cases:**
- 🏪 Retail inventory management
- 📈 Sales forecasting and planning  
- 🎯 Marketing campaign optimization
- 📦 Supply chain and logistics

---

*Last updated: October 2025*  
*Model trained on real-world ice cream sales data*
