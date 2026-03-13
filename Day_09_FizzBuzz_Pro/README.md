# Day 9: FizzBuzz Pro (Easy)

## 📝 Description

A customizable twist on the classic FizzBuzz problem! Instead of the traditional "Fizz" and "Buzz" at 3 and 5, you get to choose your own numbers and replacement words.

## 🎯 Learning Objectives

- Practice conditional logic with multiple conditions
- Understand the importance of checking order (both, then individual)
- Work with user input and validation
- Use the modulo operator (`%`) to check divisibility

## 📋 Requirements

Write a program that:
1. Asks the user for two numbers
2. Asks the user for two replacement words
3. Prints numbers 1-50, BUT:
   - If divisible by **both** numbers → print both words together
   - If divisible by the **first** number only → print the first word
   - If divisible by the **second** number only → print the second word
   - Otherwise → print the number

## 💡 Key Hint

**Check divisibility by BOTH numbers first!** If you check individual numbers first, you'll miss the "both" case.

## 🔍 Example

Enter first number: 3
Enter first word: Fizz
Enter second number: 5
Enter second word: Buzz

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
... (continues to 50)


## 🚀 Getting Started

# Get user input
num1 = int(input("Enter first number: "))
word1 = input("Enter first word: ")
# ... your code here


## ✅ Testing Your Solution

Try these test cases:
- **Classic FizzBuzz**: Numbers 3 and 5 with words "Fizz" and "Buzz"
- **Custom example**: Numbers 2 and 7 with words "Even" and "Lucky"
- **Edge case**: Same number twice (e.g., 4 and 4)

## 🎓 What You'll Learn

- Why order matters in conditional statements
- How to combine multiple boolean conditions
- The modulo operator for divisibility checks
- Building flexible, reusable programs

## 💪 Challenge Yourself

Once you've completed the basic version, try:
- Extending the range beyond 50
- Adding a third number and word
- Allowing the user to choose the range

---

**Happy Coding!** 🐍✨