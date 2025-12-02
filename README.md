# 🧠 Machine Learning Projects – End-to-End Apps & Models

> *“From notebook experiments to deployed web apps.”*  

Welcome to my **Machine Learning Projects** repository — a curated collection of end-to-end ML systems built with:

- ✅ **Classic algorithms** (Regression, Trees, SVM, XGBoost, KNN, Naive Bayes…)
- ✅ **Real datasets** (finance, health, telecom, housing, recommendations…)
- ✅ **Full pipelines** (EDA → preprocessing → training → evaluation → deployment)
- ✅ **Deployed apps** using **Flask + Render**

---

## 🏷️ Tech & Tools

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-lightgrey?logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-brightgreen)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Render](https://img.shields.io/badge/Render-Cloud%20Deployment-purple)
![Status](https://img.shields.io/badge/Projects-Active%20%26%20Growing-success)

---

## 🧭 Repository Map

```bash
Machine-Learning-projects/
├── Supervised learning/
│   ├── Regression models/
│   ├── LogisticRegression/
│   ├── DecisionTrees/              # (path name may vary in repo)
│   ├── RandomForest/
│   ├── Polynomial Regression/
│   ├── SVM/
│   └── XGBoost/
│
├── Unsupervised learning/
│   ├── K-nearest neighbors/
│   └── NaiveBase/
│
└── Unsupervised models/
    ├── K means/
    └── RecommendationSystem/
````

Each main folder has its **own README** with more details, code snippets, and usage instructions.

---

## 🚀 Live Demo Gallery

Some of the projects in this repo are deployed as **fully functional web apps**:

| Domain        | Project                                 | Live Demo                                                                                                  |
| ------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| 🏠 Housing    | Boston House Price Prediction           | [https://house-price-prediction-d58i.onrender.com](https://house-price-prediction-d58i.onrender.com)       |
| 🚗 Cars       | Car Price Predictor                     | [https://car-price-predictor-6t6e.onrender.com](https://car-price-predictor-6t6e.onrender.com)             |
| 🙂 Happiness  | Happiness Index (Income → Happiness)    | [https://machine-learning-projects-d0gh.onrender.com](https://machine-learning-projects-d0gh.onrender.com) |
| 🎗️ Health    | Simple Breast Cancer Predictor          | [https://simple-breast-cancer-predictor.onrender.com](https://simple-breast-cancer-predictor.onrender.com) |
| ❤️ Health     | Simple Heart Attack Predictor           | [https://machine-learning-projects-s5t4.onrender.com](https://machine-learning-projects-s5t4.onrender.com) |
| 🌸 Flowers    | Iris Classifier (Random Forest)         | [https://iris-classifier-vv7m.onrender.com](https://iris-classifier-vv7m.onrender.com)                     |
| 🍦 Sales      | Ice Cream Sales (Polynomial Regression) | [https://ice-cream-sales-jv5w.onrender.com](https://ice-cream-sales-jv5w.onrender.com)                     |
| 💬 NLP        | Spam vs Ham Classifier                  | [https://spamham-predictor.onrender.com](https://spamham-predictor.onrender.com)                           |
| 😃 NLP        | Emotion Detection from Text             | [https://emotions-predictor.onrender.com](https://emotions-predictor.onrender.com)                         |
| 💉 Health     | Diabetes Risk (KNN)                     | [https://knn-diabetes.onrender.com](https://knn-diabetes.onrender.com)                                     |
| 💸 Restaurant | Tip Amount (KNN Regression)             | [https://tipsamount.onrender.com](https://tipsamount.onrender.com)                                         |
| 🎬 Movies     | Movie Recommendation System             | [https://movierecommender-ovt8.onrender.com](https://movierecommender-ovt8.onrender.com)                   |

> 🔍 Each app has its **source code + model + README** inside this repository.

---

## 🎭 Supervised Learning – ML Cinematic Universe

> Folder: `Supervised learning/`

This section is a full ML zoo: regression, classification, ensembles, and boosting — all with real datasets and structured pipelines.

<details>
<summary>📊 Regression Models (Boston, Cars, Happiness)</summary>

**Folder:** `Supervised learning/Regression models/`

* 🏠 **Boston House Price Prediction**
  Predicts median house prices from socio-economic features.
  👉 Code: `Supervised learning/Regression models/Boston House/`

* 🚗 **Car Price Predictor**
  Estimates car prices from specs like brand, engine size, horsepower, etc.
  👉 Code: `Supervised learning/Regression models/Car Price predictor/`

* 🙂 **Happiness Index**
  A minimal regression pipeline: income → happiness score.
  👉 Code: `Supervised learning/Regression models/Happyness Index/`

</details>

<details>
<summary>❤️ Logistic Regression – Simple but Powerful</summary>

**Folder:** `Supervised learning/LogisticRegression/`

* 🎗️ **Breast Cancer Predictor**
  Predicts benign vs malignant tumor using logistic regression.
* ❤️ **Heart Attack Predictor**
  Classifies heart attack risk based on age.

Both projects:

* Train a **Logistic Regression** model
* Serialize it with **pickle**
* Deploy it via **Flask + Render**

</details>

<details>
<summary>🌳 Trees & Forests – Decision Trees / Random Forest</summary>

* 🌾 **Crop Recommendation System** (Decision Tree)
  Recommends crops based on soil & weather conditions.

* ❤️‍🔥 **Heart Attack Risk (Decision Tree)**
  Tree-based health classification.

* 🌸 **Iris Classifier (Random Forest)**
  Classic iris dataset with a Random Forest, deployed with a clean UI.
  👉 Code: `Supervised learning/RandomForest/Iris Classifier/`

</details>

<details>
<summary>🍦 Polynomial Regression – Ice Cream Sales</summary>

**Folder:** `Supervised learning/Polynomial Regression/Ice Cream sales/`

* Polynomial Regression (degrees 2–5)
* Interactive dashboard & charts
* REST-style API endpoints
* Deployed on Render

</details>

<details>
<summary>🛡️ SVM – Financial Risk Models</summary>

**Folder:** `Supervised learning/SVM/`

* 💳 **Credit Card Default Prediction**
* 🏦 **Universal Bank Personal Loan Prediction**

Each includes:

* PCA dimensionality reduction
* Class balancing (SMOTE / class_weight)
* GridSearchCV tuning for C, gamma, kernel
* Confusion matrices & visualizations

</details>

<details>
<summary>🚀 XGBoost – Gradient Boosting Projects</summary>

**Folder:** `Supervised learning/XGBoost/`

1️⃣ **Telco Customer Churn Prediction**

* 1,178 engineered features
* Hyperparameter-tuned XGBoost
* ROC–AUC ≈ 0.77
  👉 Code: `Supervised learning/XGBoost/TeleCustomerPred/`

2️⃣ **Titanic Survival Prediction**

* Feature engineering (Age_Category, etc.)
* Accuracy ≈ 78.8%
* ROC–AUC ≈ 0.84
  👉 Code: `Supervised learning/XGBoost/TitanicPred/`

</details>

---

## 🔍 Unsupervised Learning – Clusters & Similarities

> Folders: `Unsupervised learning/` & `Unsupervised models/`

Here live the models that **discover structure without labels**: clusters, neighbors, and recommenders.

<details>
<summary>📌 KNN Apps (Tips & Diabetes)</summary>

**Folder:** `Unsupervised learning/K-nearest neighbors/`

* 💸 **Restaurant Tip Prediction (KNN Regression)**
  👉 Path: `K-nearest neighbors/Tips/`

* 💉 **Diabetes Risk Prediction (KNN Classifier)**
  👉 Path: `K-nearest neighbors/Diabetes/`

Both use:

* Scikit-Learn Pipelines (OneHotEncoder + StandardScaler + KNN)
* Flask web apps
* Plotly visualizations
* Deployed on Render

</details>

<details>
<summary>🧠 Naive Bayes – Text Classification (NLP)</summary>

**Folder:** `Unsupervised learning/NaiveBase/`

* 😃 **Emotion Detection (Text → Emotion)**
* 📩 **Spam vs Ham Classification**

Both use:

* TF-IDF vectorization
* Multinomial Naive Bayes
* Flask apps with probability outputs
* Ready-for-deployment structure

</details>

<details>
<summary>📊 K-Means & Recommendation Systems</summary>

**Folder:** `Unsupervised models/`

* 🎗️ **Customer Segmentation (K-Means)**
  Clusters mall customers by income & spending score, plus saved KMeans model.

* 🎬 **Movie Recommendation System (Content-Based)**
  Uses genre vectors + rating distance + cosine similarity
  to recommend **similar movies instantly**, no training step.
  👉 Live demo: [https://movierecommender-ovt8.onrender.com](https://movierecommender-ovt8.onrender.com)

</details>

---

## ⚙️ How to Run Any Project Locally

Most projects follow this pattern:

```bash
# 1. Clone the repository
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git
cd "Machine-Learning-projects"

# 2. Go into a specific project folder
cd "Supervised learning/Regression models/Boston House"

# 3. (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate       # Windows

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app or notebook
python app.py                  # for Flask apps
# or
jupyter notebook               # for .ipynb files
```

Check each project’s **own README** for exact commands & options.

---

## 🧩 What This Repo Shows

By browsing this repository, you can see:

* ✅ Classic ML algorithms applied to **real, diverse problems**
* ✅ How to go from **Jupyter notebook → saved model → Flask app → Render**
* ✅ Handling:

  * Missing values & duplicates
  * Encoding & scaling
  * Class imbalance (SMOTE, resampling, class_weight)
  * Model evaluation (ROC–AUC, confusion matrix, classification report, R², MSE)
* ✅ Clean project structure for **portfolios, job applications, and academia**

---

## 👨‍💻 Author

**Awab Elkhair Abdalla (Pinkkygold)**
Machine Learning Engineer (in progress) • Electronics Engineer • UN Youth Delegate

* 🐙 GitHub: [Pinkkygold](https://github.com/Pinkkygold)
* 💼 LinkedIn: [awab-abdalla](https://www.linkedin.com/in/awab-abdalla)
* 📧 Email: `awab1355@gmail.com`

> *“Building practical ML systems that are not just accurate — but deployed, explainable, and useful.”*

⭐ If you find this repository helpful or inspiring, please **star it on GitHub** — it helps a lot and keeps more open-source ML projects coming 🚀


