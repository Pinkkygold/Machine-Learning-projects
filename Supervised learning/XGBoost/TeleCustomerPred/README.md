# 📊 Telco Customer Churn Prediction — XGBoost Model

### 🧠 Machine Learning • 📡 Telecom Analytics • 🔥 Production-Ready Model

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/XGBoost-Optimized-orange?logo=xgboost" />
  <img src="https://img.shields.io/badge/Notebook-Jupyter-yellow?logo=jupyter" />
  <img src="https://img.shields.io/badge/Model-Production%20Ready-brightgreen" />
</p>

---

## 🚀 Project Overview

This project builds a **high-performance churn prediction model** using the Telco Customer Churn dataset.
Telecom companies lose millions due to customer churn; this model predicts whether a customer is likely to leave, enabling targeted retention strategies.

The final solution includes:

* Cleaned and fully preprocessed dataset
* Automated feature engineering with one-hot encoding
* Tuned **XGBoost classifier**
* Balanced accuracy evaluation
* Visualization of ROC curve and XGBoost tree
* Exported production model (`XGboost_model.pkl`)
* Ready for integration into dashboards or web apps

---

## ⭐ Key Results

### 📈 Model Performance (Tuned XGBoost)

* **Balanced Accuracy:** **77%**
* **ROC–AUC:** **0.77**
* **Handles class imbalance** via `scale_pos_weight`
* **1,178 engineered features** after preprocessing
* **Tree visualization** exported (`xgb_tree.png`)

These results demonstrate strong predictive power for a real-world telecom environment.

---

## 🧼 Data Preprocessing Summary

The dataset was thoroughly cleaned and transformed:

* Removed non-useful identifiers (`CustomerID`, `State`, `Lat Long`, etc.)
* Fixed missing and blank values (especially `Total Charges`)
* Normalized strings for consistent encoding
* Converted booleans → integers
* One-hot encoded 18 categorical features
* Final dataset shape: **(rows, 1178 features)**

---

## 🔧 Modeling Approach

The model uses **XGBoost**, one of the strongest algorithms for tabular data.

Key modeling steps:

* Train/test split with stratification
* Baseline XGBoost model
* GridSearchCV hyperparameter tuning
* Retrained optimal model
* ROC curve evaluation
* Confusion matrix evaluation
* Model exported (`XGboost_model.pkl`)
* First decision tree visualized (`xgb_tree.png`)

---

## 🔮 Predicting New Customers

A prediction pipeline is included that:

* Accepts new customer data as a DataFrame
* Automatically aligns & encodes features
* Outputs:

  * Predicted class (0 = stays, 1 = churns)
  * Probability of leaving

This makes the model ready for dashboards, APIs, and business applications.

---

## 📁 Repository Structure

```
📦 Telco-Churn-XGBoost
│── 📄 churn_notebook.ipynb
│── 📄 Telco_customer_churn.xlsx
│── 📄 XGboost_model.pkl
│── 📄 xgb_tree.png
│── 📄 README.md
```

---

## 🛠 Technologies Used

* **Python**
* **XGBoost**
* **Pandas / NumPy**
* **Scikit-Learn**
* **Matplotlib**
* **Graphviz**
* **Pickle (model export)**

---

## 🌱 Potential Extensions

* Deploy to **Streamlit**, **Flask**, or **FastAPI**
* Add **SHAP** for model explainability
* Integrate into CRM systems
* Build an interactive BI dashboard

---

## 👨‍💻 Author

**Awab Elkhair Abdalla**
Electronics Engineer & Machine Learning Engineer

* 💼 LinkedIn: **[www.linkedin.com/in/awab-abdalla](http://www.linkedin.com/in/awab-abdalla)**
* 🐙 GitHub: **[https://github.com/Pinkkygold](https://github.com/Pinkkygold)**
* 📧 Email: **[awab1355@gmail.com](mailto:awab1355@gmail.com)**


