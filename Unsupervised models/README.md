# 🧠 Unsupervised Machine Learning – Project Collection

This folder contains a collection of **unsupervised machine learning projects**, each demonstrating real-world clustering and similarity-based recommendation techniques.
All projects include clean preprocessing, model implementation, visualization, and deployment-ready workflows.

---

<p align="center">
  <img src="https://img.shields.io/badge/Machine%20Learning-Unsupervised-blue?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Tech-Python%20%7C%20Flask%20%7C%20Render-brightgreen" />
  <img src="https://img.shields.io/badge/Developer-Awab%20Elkhair%20Abdalla-purple" />
</p>

<p align="center">
  <a href="https://github.com/Pinkkygold">
    <img src="https://img.shields.io/badge/GitHub-Pinkkygold-black?logo=github" />
  </a>
  <a href="https://www.linkedin.com/in/awab-abdalla">
    <img src="https://img.shields.io/badge/LinkedIn-Awab%20Abdalla-0A66C2?logo=linkedin" />
  </a>
</p>

---

# 📂 Projects Included in This Folder

## 1️⃣ 🎗️ Customer Segmentation Using K-Means

**GitHub:**
👉 [https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20models/K%20means](https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20models/K%20means)

A complete unsupervised ML workflow using **K-Means Clustering** to group mall customers based on:

* **Annual Income**
* **Spending Score**

### 🔍 What This Project Demonstrates

✔ Data preprocessing & cleaning
✔ Gender conversion to numeric form
✔ Elbow Method to find optimal K
✔ Cluster visualization using Matplotlib
✔ Predicting the cluster of new customers
✔ Saving the trained model with `pickle`

### 🔧 Tech Stack

* Pandas
* NumPy
* Matplotlib
* Scikit-Learn (KMeans)
* Pickle

### 📁 Project Files

* `Mall_Customers.csv`
* `CustomersWithKmeans.pkl`
* `customer_segmentation.ipynb`
* `README.md`

---

## 2️⃣ 🎬 Movie Recommendation System (Content-Based)

**Live Demo:**
👉 [https://movierecommender-ovt8.onrender.com](https://movierecommender-ovt8.onrender.com)

**GitHub:**
👉 [https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20models/RecommendationSystem](https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20models/RecommendationSystem)

A lightweight, efficient, similarity-based movie recommender system that suggests movies using:

* 🎭 **Genre vectors**
* ⭐ **Movie ratings**
* 📐 **Cosine similarity + rating distance**

### 🧠 Key Concepts in This Project

✔ One-hot vectorization of genres
✔ Average rating aggregation
✔ Cosine distance for genre similarity
✔ Highly responsive Flask web app
✔ Instant recommendations with no training
✔ Full deployment on Render Cloud

This system does **not** use supervised models — it is fully **unsupervised similarity matching**.

### 🛠️ Tech Stack

* Python
* Flask
* Pandas, NumPy
* SciPy (cosine similarity)
* HTML, CSS, Jinja2
* Render Cloud

---

# 🧩 Folder Structure

```
Unsupervised models/
│
├── K means/
│   ├── Mall_Customers.csv
│   ├── customer_segmentation.ipynb
│   ├── CustomersWithKmeans.pkl
│   └── README.md
│
└── RecommendationSystem/
    ├── movies.csv
    ├── ratings.csv
    ├── app.py (if deployed)
    ├── templates/
    ├── static/
    └── README.md
```

---

# 💡 Learning Outcomes

By exploring these projects, you gain hands-on experience in:

* Clustering algorithms
* Similarity-based recommendation systems
* Feature engineering & vectorization
* Data visualization techniques
* Web deployment with Flask
* Real-world ML app design

---

# 👨‍💻 Author

**Awab Elkhair Abdalla**
Machine Learning Engineer · Researcher · Volunteer

* 🔗 LinkedIn: [https://www.linkedin.com/in/awab-abdalla](https://www.linkedin.com/in/awab-abdalla)
* 💻 GitHub: [https://github.com/Pinkkygold](https://github.com/Pinkkygold)
* 📧 Email: **[awab1355@gmail.com](mailto:awab1355@gmail.com)**

> “Unsupervised learning helps us discover the hidden structure behind the data—
> and transform it into meaningful insights.”

---

# ⭐ Support

If these projects helped you learn or inspired you:

👉 **Please star the repository**
Your support motivates the creation of more open-source ML applications!

---
