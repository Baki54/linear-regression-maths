
<details>
<summary><b>🇧🇩 বাংলা সংস্করণ</b></summary>
  
## ধরুন, আপনার সামনে একটি Dataset রাখা হলো।

আপনাকে বলা হলো:

> ### "এই ডেটার প্যাটার্ন খুঁজে বের করুন এবং ভবিষ্যতের মান Predict করুন।"

Python, NumPy, Scikit-Learn কিংবা অন্য কোনো Machine Learning Library ব্যবহার করে হয়তো আপনি কয়েক মিনিটের মধ্যেই কাজটি করে ফেলতে পারবেন।

কি হবে যদি আপনার কম্পিউটার টিকে আপনার কাছ থেকে সরিয়ে নেওয়া হয়! এবং আপনার কাছে একটি খাতা একটি কলম এবং একটি ক্যালকুলেটর দেওয়া হয়?

তখনও কি আপনি সমস্যাটির সমাধান করতে পারবেন?

তাত্ত্বিকভাবে, সেই খাতাটিই একটি Machine Learning Model,এমনকি একটি AI Model-ও হতে পারে।

কারণ শেষ পর্যন্ত Artificial Intelligence মূলত সংখ্যা, সমীকরণ, ম্যাট্রিক্স, সম্ভাব্যতা, ক্যালকুলাস, টেনসর এবং অসংখ্য গাণিতিক গণনার সমষ্টি।

---

## সমস্যা কোথায়?

বর্তমানে Machine Learning শেখার সবচেয়ে জনপ্রিয় উপায় হলো Library ব্যবহার করা।

```python
model.fit(X, y)

prediction = model.predict(X)
```

কোড চলে।

মডেল ট্রেইন হয়।

Prediction পাওয়া যায়।

কিন্তু এরপর?

* এটি কেন কাজ করল?
* এর পেছনের গণিত কি?
* Prediction কীভাবে তৈরি হলো?
* Regression Line কোথা থেকে এলো?
* Cost Function কী?
* Error কেন কমলো?
* Gradient Descent কী করছে?
* SVM কেন কাজ করে?
* Neural Network আসলে কী শিখছে?

অনেক সময় আমরা এসব প্রশ্ন করি না, অথবা উত্তরগুলো জানি না।

ফলে আমরা Library ব্যবহার করতে শিখি, কিন্তু অ্যালগরিদমকে বুঝতে শিখি না।

---

## এই সিরিজের উদ্দেশ্য

এই সিরিজে আমরা Machine Learning-কে একটি Library হিসেবে নয়, বরং একটি গাণিতিক ধারণা হিসেবে বোঝার চেষ্টা করব।

প্রতিটি অ্যালগরিদমকে শূন্য থেকে গাণিতিকভাবে বিশ্লেষণ করা হবে, তারপর Python দিয়ে বাস্তবায়ন করা হবে—কোনো Machine Learning Library ব্যবহার ছাড়াই।

লক্ষ্য একটাই:

❌ How to use it?

✅ How does it work?

---

## এই সিরিজে যা থাকবে

* Linear Regression
* Polynomial Regression
* Support Vector Regression (SVR)
* Logistic Regression
* K-Nearest Neighbors (KNN)
* Naive Bayes
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* K-Means Clustering
* Neural Networks
* Backpropagation
* Gradient Descent
* Transformers
* Large Language Models (LLM)

এবং প্রতিটি বিষয়ের পেছনের গাণিতিক ভিত্তি।




> **Don't learn Machine Learning as a library. Learn it as mathematics.**

---

<summary><b>  English version</b></summary>

</details>


## Imagine someone gives you a dataset and asks:

>### "Find the pattern in this data and predict future values."

Using Python, NumPy, Pandas, and Scikit-Learn, you could probably solve the problem within minutes.

But what if your computer was taken away and you were given a notebook, a pen, and a calculator?

Could you still do it?

**Theoretically, that notebook could become a Machine Learning model,even an Artificial Intelegence model.**

In fact, if you had enough time and patience, it could even simulate the mathematical computations behind modern AI systems.

Because at its core, Everything is mathematics.

Every prediction, classification, recommendation, generated image, or generated sentence is ultimately the result of numbers, matrices, probabilities, calculus, tensor and mathematical transformations.

---

## The Problem

Today, many people start learning Machine Learning through libraries.

```python
model.fit(X, y)
prediction = model.predict(X)
```

The model works.

The prediction appears.

Everything seems fine.

But then questions arise:

* Where did the regression line come from?
* Why does the error decrease?
* What exactly is a cost function?
* How does gradient descent work?
* Why does SVM work?
* What is a neural network actually learning?

Unfortunately, many learners never explore these questions deeply.

As a result, they learn how to use algorithms, but not how the algorithms actually work.

---

## Purpose of This Repository

This repository is **not** another Machine Learning library.

Its purpose is to explore and explain the mathematics behind Machine Learning algorithms from the ground up.

The goal is simple:

❌ How to use it?

✅ How does it work?

Each algorithm is broken down into its mathematical foundations before being implemented in Python.

The focus is not on hiding complexity.

The focus is on understanding it.

---


Real understanding begins when you can answer questions such as:

* Where does the equation come from?
* Whats the maths behind of it?
* Why does the algorithm work?
* How is the prediction generated?
* Can I implement it myself without relying entirely on a library?

This project is not about creating library users.

It is about creating learners who understand the foundations.

---

## Topics Covered

This is an ongoing educational series that aims to cover the mathematics behind:

* Linear Regression
* Multiple Linear Regression
* Polynomial Regression
* Logistic Regression
* K-Nearest Neighbors (KNN)
* Naive Bayes
* Decision Trees
* Random Forests
* Support Vector Machines (SVM)
* Support Vector Regression (SVR)
* K-Means Clustering
* Principal Component Analysis (PCA)
* Neural Networks
* Backpropagation
* Gradient Descent
* Transformers
* Large Language Models (LLMs)

Everything will do without any mechine learning librery, just mathematics and pure python.

**The mathematics will makes them work.**

---

If your goal is not only to train models, but also to understand them, then this serise is for you.


## Don't learn Machine Learning as a library. Learn it as mathematics.
