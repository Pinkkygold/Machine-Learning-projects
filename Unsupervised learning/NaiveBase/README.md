
# 🧠 Naive Bayes Text Classification Suite

This folder contains a mini–collection of **Naive Bayes–based NLP projects** built with Python and Scikit-Learn.  
Each project focuses on a real-world text classification problem and is designed to be:

- 🔍 Easy to understand
- 🧪 Simple to experiment with
- 🚀 Ready to deploy as a web app

---

## 📂 Projects in this Folder

### 1️⃣ Emotion Detection (Text → Emotion)

Predicts the **emotion** expressed in a sentence (e.g. joy, sadness, anger).

- 📁 Project path:  
  `Unsupervised learning/NaiveBase/Emotions`
- 🔗 GitHub:  
  https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/NaiveBase/Emotions
  - 🌐 Live Demo (Render):  
  https://emotions-predictor.onrender.com

**Highlights:**

- Text preprocessing and TF-IDF vectorization  
- Naive Bayes classifier for multi-class emotion labels  
- Flask web app with probability visualization  
- `/api/predict` endpoint for programmatic access

---

### 2️⃣ Spam vs Ham Classifier (SMS / Email)

Classifies text messages as **Spam** or **Ham** (legitimate).

- 📁 Project path:  
  `Unsupervised learning/NaiveBase/SpamHam`
- 🔗 GitHub:  
  https://github.com/Pinkkygold/Machine-Learning-projects/tree/main/Unsupervised%20learning/NaiveBase/SpamHam
  - 🌐 Live Demo (Render): https://spamham-predictor.onrender.com

**Highlights:**

- TF-IDF + Naive Bayes for spam detection  
- Clean Flask interface  
- Shows predicted label and confidence (when `predict_proba` is available)  
- Ready for deployment on Render (or any WSGI server)

---

## 🧱 Shared Tech Stack

Both projects are built around a similar architecture:

- 🐍 Python 3.x  
- 📦 Scikit-Learn (Naive Bayes, Pipelines, TF-IDF)  
- 💬 NLP preprocessing (lowercasing, tokenization, stopword removal, etc.)  
- 🌐 Flask web framework  
- ⚙️ Gunicorn (for production deployment)  
- ☁️ Render (for cloud hosting)

This makes the folder a good **learning path** for:

- Going from **Jupyter training notebook → saved model (`pickle`) → Flask app → deployment**
- Reusing the same pattern for future text classification projects

---

## 🚀 How to Run Any Project Locally

> Below is a generic guide that works for both `Emotions` and `SpamHam`.  
> Just `cd` into the corresponding folder before running the commands.

```bash
# 1. Clone the main repository
git clone https://github.com/Pinkkygold/Machine-Learning-projects.git

# 2. Go to the NaiveBase folder
cd "Machine-Learning-projects/Unsupervised learning/NaiveBase"

# 3. Move into one of the projects
cd Emotions        # or: cd SpamHam

# 4. (Optional) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS / Linux
# .venv\Scripts\activate       # Windows

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run the Flask app
python app.py
````

Then open:

```text
http://127.0.0.1:5000
```

---

## 📊 Typical ML Pipeline (Naive Bayes Text Classifier)

All projects roughly follow this pattern:

1. **Load & explore dataset**
2. **Preprocess & clean text**
   (e.g. lowercasing, removing punctuation, handling missing values)
3. **Vectorize text using TF-IDF**
4. **Train a Naive Bayes classifier**
   (e.g. `MultinomialNB`)
5. **Evaluate performance**
   (accuracy, confusion matrix, classification report)
6. **Export trained model** to a `.pkl` file:

   ```python
   import pickle

   with open("model.pkl", "wb") as f:
       pickle.dump(model, f)
   ```
7. **Build Flask app** that:

   * Loads the model
   * Accepts user text input
   * Returns predictions and confidence
8. **Deploy to cloud** (e.g. Render) with:

   * `requirements.txt`
   * `app.py`
   * `gunicorn app:app`

---

## 💡 How to Use This Folder

You can think of `NaiveBase` as your **template hub** for:

* Creating new Naive Bayes NLP projects
* Copying the pattern (notebook → model → Flask → Render)
* Demonstrating end-to-end ML deployment in your portfolio

Ideas for extension:

* 🔁 Add more Naive Bayes projects (e.g. sentiment analysis)
* 🌍 Add multilingual support (Arabic, Turkish, English)
* 🧪 Compare Naive Bayes vs Logistic Regression vs SVM
* 📈 Add Plotly visualizations to all web apps

---

## ✨ About the Author

Created and maintained by **Awab Elkhair Abdalla Idris (Pinkkygold)**
Machine Learning Engineer in progress | AI for social impact | UN Youth Delegate

* GitHub: [https://github.com/Pinkkygold](https://github.com/Pinkkygold)
* LinkedIn: *(add your LinkedIn link here)*

If you like this structure, feel free to ⭐ the repo and reuse the pattern in your own projects.


