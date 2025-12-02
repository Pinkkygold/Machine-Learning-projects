# ⛴️ Titanic Survival Prediction — XGBoost Model  
### 🧠 Binary Classification • 🎯 Survival Prediction • 🔥 Gradient Boosting

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Model-XGBoost-orange?logo=xgboost" />
  <img src="https://img.shields.io/badge/Dataset-Titanic%20(seaborn)-lightgrey" />
  <img src="https://img.shields.io/badge/Accuracy-78.8%25-brightgreen" />
  <img src="https://img.shields.io/badge/ROC--AUC-0.84-success" />
</p>

---

## 🚀 Project Overview

This project builds a **machine learning model** to predict whether a passenger on the **Titanic** survived or not, using the classic Titanic dataset from `seaborn`.

The workflow includes:

- Exploratory data analysis & cleaning  
- Feature engineering (age category, encoding categorical variables)  
- Training an **XGBoost classifier**  
- Model evaluation with accuracy, classification report, confusion matrix, and ROC–AUC  
- A simple prediction pipeline for new passenger data  
- Exporting the trained model as `TitanicXGB.pkl` for reuse or deployment  

---

## 📊 Dataset

- Source: `sns.load_dataset("titanic")`
- Shape: **891 rows × 15 columns**
- Target: `survived`  
  - `0` → did not survive  
  - `1` → survived  

Features used in the final model include:

- Passenger class (`pclass`)  
- Sex (`sex`)  
- Age  
- Siblings/spouses aboard (`sibsp`)  
- Parents/children aboard (`parch`)  
- Ticket fare (`fare`)  
- Who (`who`: man/woman/child)  
- Adult male flag (`adult_male`)  
- Embarkation town (`embark_town`)  
- Alone flag (`alone`)  
- Engineered feature: **Age_Category** (Young / Teen / Adult / Middle / Senior)

---

## 🧼 Data Cleaning & Feature Engineering

Key preprocessing steps:

- Handled missing values:
  - `age` imputed with mean
  - `embark_town` imputed with most frequent value (mode)
- Dropped high-missing or redundant columns:
  - `embarked`, `class`, `deck`, `alive`
- Removed duplicate rows  
- Created **Age_Category** based on age ranges (child, teen, adult, etc.)  
- Converted categorical variables into numeric representations using label encoding  
- Final clean dataset: **780 rows × 12 columns**

---

## 🔧 Modeling Approach

- Split into **train** and **test** sets (80% / 20%)  
- Trained an **XGBoostClassifier** on the processed features  
- Model saved as **`TitanicXGB.pkl`** using `pickle` for future inference  
- Simple prediction example implemented:
  - New passenger data (e.g., a 45-year-old male in 3rd class)  
  - Model outputs:  
    - `0` → Not Survived  
    - `1` → Survived  

---

## 📈 Model Performance

On the held-out test set:

- ✅ **Accuracy:** **≈ 78.85%**  
- ✅ **ROC–AUC:** **0.8372**  

**Classification report (summary):**

- Class **0 (Not Survived)**  
  - Good precision, recall, and F1-score  
- Class **1 (Survived)**  
  - Competitive precision and recall (~0.72–0.76 range)

**Visual evaluations (generated in the notebook):**

- 📊 **Confusion Matrix** – to understand true/false positives/negatives  
- 📈 **ROC Curve** – illustrating tradeoff between TPR and FPR  

---

## 🔮 Inference & Prediction

The project includes a simple pipeline to:

1. Accept new passenger data as a numerical feature vector  
2. Run it through the trained **XGBoost** model  
3. Return:
   - Predicted class: **“Survived”** or **“Not Survived”**  
   - Under the hood, uses `model.predict()` and `model.predict_proba()`  

This setup can easily be integrated into:

- A **Streamlit** or **Flask** app  
- A REST API for real-time prediction  
- A teaching demo for ML classification

---

## 📁 Repository Structure

```bash
Titanic-XGBoost/
│
├── TitanicXGB.pkl           # Saved XGBoost model
├── titanic_notebook.ipynb   # Full EDA, preprocessing & modeling
├── README.md                # Project documentation
└── (optional) figures/
    ├── roc_curve.png
    └── confusion_matrix.png
````

---

## 🛠 Tech Stack

* **Python**
* **Pandas**, **NumPy**
* **Seaborn**, **Matplotlib**
* **Scikit-Learn** (metrics, splitting)
* **XGBoost**
* **Pickle** (model serialization)

---

## 🌱 Possible Extensions

* Hyperparameter tuning (GridSearchCV / RandomizedSearchCV)
* Add cross-validation and calibration
* Use SHAP for explainable AI (feature importance per passenger)
* Deploy via **Streamlit** or **FastAPI**

---

## 👨‍💻 Author

**Awab Elkhair Abdalla**
Electronics Engineer & Aspiring Machine Learning Engineer

* 💼 LinkedIn: [linkedin.com/in/awab-abdalla](https://www.linkedin.com/in/awab-abdalla)
* 🐙 GitHub: [github.com/Pinkkygold](https://github.com/Pinkkygold)
* 📧 Email: [awab1355@gmail.com](mailto:awab1355@gmail.com)

