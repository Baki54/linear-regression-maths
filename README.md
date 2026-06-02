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

---



> **Don't learn Machine Learning as a library. Learn it as mathematics.**
