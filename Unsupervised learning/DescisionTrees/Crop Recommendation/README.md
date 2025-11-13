# 🌾 Crop Recommendation System

### *(Machine Learning + Flask Web App + Render Deployment)*

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)]()
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)]()
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML%20Models-orange?logo=scikit-learn)]()
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)]()
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy)]()
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?logo=render)](https://croprecommendation-nt2w.onrender.com)

---

## 🌐 **Live Demo**

👉 **[https://croprecommendation-nt2w.onrender.com](https://croprecommendation-nt2w.onrender.com)**

---

## 📌 **Project Overview**

This is a **Machine Learning–powered Crop Recommendation System** that helps farmers choose the **best crop** to grow based on soil and environmental conditions.

Using **Decision Tree Classifier**, the model predicts the most suitable crop by analyzing:

* Nitrogen (N)
* Phosphorus (P)
* Potassium (K)
* Temperature
* Humidity
* pH level
* Rainfall

The system is deployed as a **Flask Web Application** and hosted on **Render Cloud**.

---

## 🧠 **Model Details**

### ✔ Algorithm Used

**Decision Tree Classifier**
Criterion: `entropy`

### ✔ Preprocessing

* Handled duplicates/missing values
* Standardized features using **StandardScaler**
* Correlation analysis + boxplots + heatmap

### ✔ Accuracy Achieved

The model performs strongly on the dataset and provides reliable crop predictions.

### ✔ Saved Artifacts

* `Cropmodel.pkl` — trained ML model
* `scaler.pkl` — StandardScaler for preprocessing

---

## 📊 **Dataset Information**

The dataset contains soil nutrients and environmental features mapped to crop labels.

| Feature     | Description                |
| ----------- | -------------------------- |
| N           | Nitrogen content (mg/kg)   |
| P           | Phosphorus content (mg/kg) |
| K           | Potassium content (mg/kg)  |
| Temperature | in °C                      |
| Humidity    | %                          |
| pH          | Soil acidity/alkalinity    |
| Rainfall    | mm                         |
| Label       | Crop name                  |

---

## 🖥 **Tech Stack**

### 🔧 Backend & ML

* Python
* Scikit-learn
* NumPy
* Pandas
* Pickle

### 🌐 Frontend

* HTML
* CSS

### 🚀 Deployment

* Flask
* Render Cloud Hosting

---

## 📁 Folder Structure

```
CropRecommendation/
│
├── app.py
├── Cropmodel.pkl
├── scaler.pkl
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

---

## ▶️ **How to Run the Project Locally**

Clone the repository:

```bash
git clone https://github.com/yourusername/CropRecommendation.git
cd CropRecommendation
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🚀 Deployment on Render

1. Create a Render account
2. Upload your repo
3. Add:

   ```
   gunicorn app:app
   ```
4. Add **requirements.txt**
5. Deploy 🎉

---

## 🌱 **Prediction Example**

Input:

```
N = 111
P = 11
K = 50
Temperature = 30
Humidity = 90
pH = 8
Rainfall = 40
```

Output:

```
Rice
```



---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📝 License

This project is open-source under the **MIT License**.

---
