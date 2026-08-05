# 🏆 Student Performance Analyzer

A beginner-friendly Python mini project that analyzes student marks using **dictionaries and built-in Python functions**.

## 📌 Project Overview

The **Student Performance Analyzer** takes a dictionary containing student names and their marks and performs several useful operations, such as finding the topper, finding the lowest scorer, sorting students by marks, checking pass conditions, and calculating the average marks.

This project is designed to practice working with **dictionaries, `max()`, `min()`, `sorted()`, `all()`, `any()`, `sum()`, and `len()`**.

## 📊 Given Data

```python
students = {
    "Aman": 82,
    "Riya": 91,
    "Karan": 67,
    "Priya": 88,
    "Neha": 75
}
```

## 🎯 Features

The program performs the following tasks:

* 🥇 Finds and prints the **topper**
* 📉 Finds and prints the **lowest scorer**
* 📊 Sorts students according to their marks
* ✅ Checks whether **all students passed** (marks ≥ 35)
* 🌟 Checks whether **any student scored above 90**
* 📈 Calculates and displays the **average marks**

## 🛠️ Python Concepts Used

* Dictionaries
* `dict.items()`
* `dict.values()`
* `max()`
* `min()`
* `sorted()`
* `all()`
* `any()`
* `sum()`
* `len()`
* Lambda functions

## 💡 Example Output

```text
Topper: Riya - 91
Lowest Scorer: Karan - 67

Students sorted by marks:
Karan: 67
Neha: 75
Aman: 82
Priya: 88
Riya: 91

All students passed: True
Any student scored above 90: True
Average Marks: 80.6
```

## 📚 What I Learned

Through this project, I practiced how to:

* Access dictionary keys and values
* Work with `items()` to handle keys and values together
* Find maximum and minimum values in a dictionary
* Sort dictionary data based on values
* Use `all()` and `any()` for conditions
* Calculate an average using `sum()` and `len()`
* Use built-in Python functions instead of manually writing loops

## 🚀 How to Run

1. Make sure Python is installed.
2. Open the project in VS Code or any Python editor.
3. Run the Python file:

```bash
python student_performance_analyzer.py
```

## 🏁 Conclusion

This mini project demonstrates how Python's built-in functions can make dictionary-based data analysis simple and efficient. It is a small practical example of how student data can be processed and analyzed using Python.
