# 🌳 Decision Tree Classifier Projects

### *(Supervised Machine Learning — Classification with Scikit-Learn)*

This section of the repository contains projects built using Decision Tree Classifiers trained on different datasets to solve real-world classification problems.
Each project includes data preprocessing, EDA, model training, evaluation, and prediction — following a clean and organized workflow.

---

## 📂 Projects Included

---

### 1️⃣ Crop Recommendation System

A machine learning model that predicts the most suitable crop to grow based on soil nutrients and environmental conditions.

**Tech Used:**
Python, Scikit-Learn, DecisionTreeClassifier (entropy), Pandas, NumPy, StandardScaler, Flask, Render Deployment

🔗 Live App:
[https://croprecommendation-nt2w.onrender.com](https://croprecommendation-nt2w.onrender.com)

📁 Folder:
[https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/DescisionTrees/Crop%20Recommendation](https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/DescisionTrees/Crop%20Recommendation)

<br>

**Features:**

* Soil nutrient analysis (N, P, K)
* Temperature, humidity, pH, rainfall
* Recommends crops such as rice, maize, lentil, cotton, etc.

---

### 2️⃣ Heart Attack Risk Prediction using Decision Tree

A classification model predicting the likelihood of heart attack based on patient health metrics.

**Tech Used:**
Python, Scikit-Learn, Decision Tree, Class Balancing, Flask

🔗 Live App:
[https://hearattack-with-decisiontree.onrender.com](https://hearattack-with-decisiontree.onrender.com)

📁 Folder:
[https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/DescisionTrees/HearAttack%20with%20DecisionTree](https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/DescisionTrees/HearAttack%20with%20DecisionTree)

<br>

**Features:**

* Gender, cholesterol, fasting sugar, resting ECG, peak slope
* Visualization with Matplotlib & Seaborn
* Train/test performance evaluation

---

## 🧠 Why Decision Trees?

Decision Trees are:

* Easy to understand and visualize
* Work well with numerical and categorical features
* Require minimal data preprocessing
* Useful for baseline classification models
* Provide strong feature importance insights

---

## 🛠 ML Workflow Used in All Projects

1. Load and explore dataset (EDA)
2. Remove duplicates, check for missing values
3. Visualizations (boxplots, heatmaps)
4. Train-test split
5. Feature scaling (when needed)
6. Train Decision Tree (`criterion='entropy'`)
7. Evaluate model
8. Save model using Pickle
9. Optional Flask deployment

---

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git
cd Machine-Learning-projects/Unsupervised learning/DescisionTrees
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run any Jupyter notebook:

```bash
jupyter notebook
```

---

## 🤝 Contributions

Feel free to open issues or submit pull requests — improvements are always welcome.

---

## 📧 Contact

If you’re working on ML or data-driven agriculture and would like to collaborate, feel free to reach out.

---
