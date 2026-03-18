# Day 12: Student Grade Book 📚

Welcome to Day 12 of your Python journey! Today you'll build a **Student Grade Book** system to practice working with dictionaries and data analysis.

---

## 🎯 Project Goal

Create a program that manages student grades, calculates averages, and identifies top performers using dictionaries and lists.

---

## 📋 Requirements

### Core Features:
1. **Store student data** - Use a dictionary with student names as keys and lists of scores as values
2. **Calculate individual averages** - Find each student's average score
3. **Find the top student** - Identify who has the highest average
4. **Find the bottom student** - Identify who has the lowest average
5. **Calculate class average** - Find the overall average across all students

---

## 💡 Key Concepts

### Dictionary Structure:
grades = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 95],
    "Charlie": [70, 75, 80]
}


### Calculating Average:
average = sum(scores) / len(scores)


### Finding Max/Min with Lambda:
top_student = max(grades, key=lambda name: sum(grades[name])/len(grades[name]))


---

## 🚀 Getting Started

1. Create a dictionary to store student names and their scores
2. Add at least 3-5 students with 3-5 test scores each
3. Loop through and calculate each student's average
4. Use `max()` and `min()` functions to find top/bottom performers
5. Calculate the overall class average

---

## 📝 Example Output

=== Student Grade Book ===

Alice's average: 85.00
Bob's average: 91.00
Charlie's average: 75.00

Top student: Bob (91.00)
Bottom student: Charlie (75.00)
Class average: 83.67


---

## 🎓 Bonus Challenges

- Add letter grades (A, B, C, etc.) based on averages
- Allow user input to add new students
- Find students above/below class average
- Add functionality to add new test scores