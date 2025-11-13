💳 Universal Bank Loan Prediction (SVM + PCA + SMOTE)

Python Scikit-Learn Pandas NumPy Matplotlib License: MIT

🧠 Project Overview

This notebook demonstrates an end-to-end machine learning pipeline for predicting whether a bank customer will accept a personal loan offer.

The workflow integrates:

SVM (Support Vector Machine) for classification
PCA for dimensionality reduction
SMOTE for class-imbalance correction
GridSearchCV for hyperparameter optimization
⚙️ Tech Stack & Libraries

Category	Tools & Libraries
Programming	Python
Data Manipulation	Pandas, NumPy
Visualization	Matplotlib, Seaborn
ML Modeling	Scikit-learn (SVC, PCA, GridSearchCV), imbalanced-learn (SMOTE)
Notebook	Jupyter (.ipynb)
📊 Dataset Description

The Universal Bank dataset contains customer demographics and financial behavior features used to predict loan acceptance.

Feature	Description
Age, Experience, Income	Demographics
CCAvg	Average monthly credit card spending
Mortgage	Mortgage value
Securities Account, CD Account, Online, CreditCard	Binary indicators
Personal Loan	Target (1 = accepted, 0 = not accepted)
🔍 Workflow Summary

🧩 Step 1: Data Preprocessing

Handled missing values, outliers, and feature scaling
⚖️ Step 2: Imbalance Handling

Applied SMOTE to oversample minority class
📉 Step 3: Dimensionality Reduction

Used PCA (95% variance) to eliminate redundancy
🧪 Step 4: Model Tuning

GridSearchCV tested multiple hyperparameter combinations:

'C': [1, 10, 100]
'gamma': ['scale', 0.1, 0.01, 0.001]
'kernel': ['rbf']
'class_weight': [None, 'balanced']
📈 Step 5: Model Evaluation

Metric	Class 0	Class 1
Precision	0.71	0.29
Recall	0.89	0.11
F1-score	0.79	0.16
Accuracy: 0.66 Best Params: C=10, gamma=0.001, kernel='rbf', class_weight='balanced'

📊 Visualizations

PCA Scree Plot
Confusion Matrix Heatmap
SVM Decision Surface (2D PCA Projection) (screenshots or plots can be added here)
🧠 Insights

PCA + SMOTE improved model balance and interpretability.
SVM achieved high accuracy for the majority class but struggled with minority recall.
Adding class_weight='balanced' improved minority detection.
🚀 Run Locally

# Clone repo
git clone https://github.com/<your-username>/SVM_Universal_Bank.git
cd SVM_Universal_Bank

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook SVM_Universal_Bank.ipynb
📦 Requirements

numpy
pandas
matplotlib
seaborn
scikit-learn
imbalanced-learn
🧭 Future Improvements

Try XGBoost or Random Forest for interpretability
Add Flask web interface for deployment
Evaluate using precision-recall AUC
Explore SMOTEENN / ADASYN for better synthetic samples
👨‍💻 Author

Awab Elkhair Abdalla Idris 🎓 Electronics & Computer Engineer | 🤖 Machine Learning Engineer | 🌍 UN Youth Delegate

GitHub LinkedIn

🪪 License

Licensed under the MIT License.

⭐ If you like this project, please star the repo!
