
# 🌟 **Customer Segmentation Using K-Means Clustering**


---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/ML-KMeans-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-yellow?logo=plotly" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas" />
  <img src="https://img.shields.io/badge/Numpy-Vectorization-red?logo=numpy" />
  <img src="https://img.shields.io/badge/Status-Completed-success?logo=check" />
</p>

<p align="center">
  <a href="www.linkedin.com/in/awab-abdalla">
    <img src="https://img.shields.io/badge/Connect%20with%20me-LinkedIn-blue?logo=linkedin" />
  </a>
  <a href="mailto:awab1355@gmail.com">
    <img src="https://img.shields.io/badge/Contact-Email-red?logo=gmail" />
  </a>
</p>

---

## 🧠 **Project Overview**

Customer segmentation is one of the most powerful applications of unsupervised learning.
In this project, I applied **K-Means Clustering** to group mall customers based on:

* **Annual Income**
* **Spending Score**

The goal is to help businesses better understand their customer base, optimize marketing strategies, and build targeted campaigns.

---

## 📊 **Key Features**

✔ Cleaned and preprocessed the dataset
✔ Converted gender to numeric format
✔ Used **Elbow Method** to find optimal K
✔ Visualized clusters and centroids
✔ Predicted cluster membership for new customers
✔ Saved trained model using `pickle`

---

## 🚀 **Technologies Used**

| Library          | Purpose                  |
| ---------------- | ------------------------ |
| **Pandas**       | Data handling            |
| **NumPy**        | Numerical operations     |
| **Matplotlib**   | Visualization            |
| **Scikit-Learn** | K-Means clustering       |
| **Pickle**       | Saving the trained model |

---

## 📈 **Elbow Method Plot**

> Helps select the optimal number of clusters.

```
for k in range(1,11): 
    km= KMeans(n_clusters=k, random_state=42) 
    km.fit(x) 
    ssd.append(km.inertia_)
```

---

## 🎯 **Customer Segmentation Visualization**

* Each dot → customer
* Colors → cluster membership
* Red "X" → cluster centers
* Labels → cluster names

```
plt.scatter(x.iloc[:,0], x.iloc[:,1], c=pred, cmap='summer')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=200, c='red', marker='X')
```

---

## 🔮 **Predicting New Customer Cluster**

```
new_data = np.array([200, 100]).reshape(1,-1)
prediction = kmeans.predict(new_data)
```

✔ The model assigns the customer to the nearest cluster based on income + spending behavior.

---

## 💾 **Saving the Trained Model**

```
with open('CustomersWithKmeans.pkl', 'wb') as f:
    pickle.dump(kmeans, f)
```

This allows deployment in Flask/Streamlit or integration into dashboards.

---

## 📁 **Project Structure**

```
├── Mall_Customers.csv
├── CustomersWithKmeans.pkl
├── customer_segmentation.ipynb
├── README.md
└── images/
```

(Optional: I can create an `images/` folder with graphs and embed them.)

---

## 📬 **Contact**

💼 LinkedIn: **[www.linkedin.com/in/awab-abdalla](http://www.linkedin.com/in/awab-abdalla)**
📨 Email: **[awab1355@gmail.com](mailto:awab1355@gmail.com)**

---

## ⭐ **If you found this project helpful, consider giving it a star!**

<p align="center">
  ⭐⭐⭐⭐⭐  
</p>

---
