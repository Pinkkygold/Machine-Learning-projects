# 💳 Credit Card Default Prediction

### *(SVM • PCA • Downsampling • GridSearchCV)*

[![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Linear%20Algebra-013243?logo=numpy)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c)](https://matplotlib.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📘 Project Overview

This project builds a **Credit Card Default Prediction** model using:

* **Support Vector Machine (SVM)**
* **PCA (Principal Component Analysis)** for dimensionality reduction
* **Downsampling** to correct **class imbalance**
* **GridSearchCV** for hyperparameter tuning
* **Decision Surface Visualization** using first two PCA components

The goal is to classify whether a credit card user will **default next month** (1) or **not default** (0).

📁 The implementation is fully contained in:
👉 **`Credit_card.ipynb`**

---

## 📂 Dataset Summary

The dataset (`default of credit card clients.csv`) includes:

* **Demographic data**: age, education, marriage status, gender
* **Payment history**: PAY_0 … PAY_6
* **Bill amounts**: BILL_AMT1 … BILL_AMT6
* **Payment amounts**: PAY_AMT1 … PAY_AMT6
* **Target variable**: `DEFAULT` (0 = no default, 1 = default)

---

## 🧪 Methodology

### **1️⃣ Data Cleaning**

* Removed invalid values (`EDUCATION=0`, `MARRIAGE=0`)
* Dropped the `ID` column

### **2️⃣ Downsampling (Balancing the Dataset)**

The dataset is highly imbalanced, so we downsample both classes to 1000 each:

```python
df_no_default_downsampled = resample(df_no_default, n_samples=1000, replace=False)
df_default_downsampled = resample(df_default, n_samples=1000, replace=False)
df_downsample = pd.concat([df_no_default_downsampled, df_default_downsampled])
```

### **3️⃣ Encoding**

All categorical columns were one-hot encoded.

### **4️⃣ Feature Scaling**

Used:

```python
from sklearn.preprocessing import scale
X_train_scaled = scale(X_train)
X_test_scaled = scale(X_test)
```

### **5️⃣ Modeling — SVM**

Baseline model:

```python
clf_svm = SVC()
clf_svm.fit(X_train_scaled, y_train)
```

### **6️⃣ Hyperparameter Tuning (GridSearchCV)**

Tuned:

* `C = [0.5, 1, 10, 100]`
* `gamma = ['scale', 1, 0.1, 0.01, 0.001, 0.0001]`
* `kernel = ['rbf']`

Best result:

```python
{'C': 100, 'gamma': 0.001, 'kernel': 'rbf'}
```

### **7️⃣ PCA + Scree Plot**

Identifying how much variance each component explains.

### **8️⃣ 2D Decision Surface Visualization**

Used PCA components 1 & 2 to visualize SVM decision regions.

---

## 📈 Results

### 🔹 **Classification Report**

```
Accuracy: 0.66

Class 0 — No Default
Precision: 0.71
Recall: 0.89
F1-score: 0.79

Class 1 — Default
Precision: 0.29
Recall: 0.11
F1-score: 0.16
```

### 🔹 **Insights**

* The SVM performs well on the majority of “No Default” cases
* It struggles with minority “Default” cases (typical for financial datasets)
* Downsampling helps, but more advanced balancing methods (SMOTE, class weights) could improve Class 1 recall

---

## 🎨 Visualizations

### ✔️ Scree Plot

Shows how much variance PCA components capture.

### ✔️ PCA Decision Boundary

Visual 2D decision regions of SVM using PC1 & PC2.

*(Add your plot images here after generating them)*

---

## 🚀 Predicting New Data

The model expects **encoded + scaled** input.

### Use this helper function:

```python
def predict_new_customer(raw_list):
    df_new = pd.DataFrame([raw_list], columns=X.columns)
    df_new_enc = pd.get_dummies(df_new).reindex(columns=X_encoded.columns, fill_value=0)
    df_new_scaled = scale(df_new_enc)
    return clf_svm.predict(df_new_scaled)[0]
```

---

## ⚙️ Installation & Running

```bash
# Clone repo
git clone https://github.com/<your-username>/Credit_Card_Default_SVM.git
cd Credit_Card_Default_SVM

# Install dependencies
pip install -r requirements.txt

# Run notebook
jupyter notebook Credit_card.ipynb
```

---

## 📦 Requirements

```
numpy
pandas
matplotlib
seaborn
scikit-learn
imbalanced-learn
```

---

## 🧭 Future Improvements

* ✔️ Try SMOTE / SMOTEENN instead of downsampling
* ✔️ Try Logistic Regression, Random Forest, XGBoost
* ✔️ Try SVM with `class_weight='balanced'`
* ✔️ Build a Flask API for predictions
* ✔️ Deploy model on Render or HuggingFace Spaces

---

## 👨‍💻 Author

**Awab Elkhair Abdalla Idris**
Machine Learning Engineer • UN Youth Delegate • Researcher

🔗 GitHub: [https://github.com/Pinkkygold](https://github.com/Pinkkygold)
🔗 LinkedIn: [https://linkedin.com/in/awab-elkhair](https://linkedin.com/in/awab-elkhair)

---

## 🪪 License

This project is licensed under the MIT License.

---

⭐ *If you like this repo, don’t forget to star it!* ⭐

---
