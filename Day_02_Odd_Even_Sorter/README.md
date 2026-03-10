# 📋 Even/Odd Number Sorter

A simple Python project that sorts 10 user-inputted numbers into two separate lists: even numbers and odd numbers.

## 🎯 Project Overview

This beginner-friendly program demonstrates fundamental Python concepts including:
- User input handling
- Loops and iteration
- Conditional statements
- List operations
- Basic arithmetic operations (modulo)

## 🚀 How It Works

1. The program prompts the user to enter 10 numbers
2. Each number is checked to determine if it's even or odd
3. Even numbers (divisible by 2) are added to the `evens` list
4. Odd numbers are added to the `odds` list
5. Both lists are displayed at the end

## 💻 Sample Code

# Initialize empty lists
evens = []
odds = []

# Get 10 numbers from user
for i in range(10):
    number = int(input(f"Enter number {i + 1}: "))
    
    # Check if even or odd
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)

# Display results
print("\n📊 Results:")
print(f"Even numbers: {evens}")
print(f"Odd numbers: {odds}")


## 🎮 Example Run

Enter number 1: 5
Enter number 2: 12
Enter number 3: 7
Enter number 4: 20
Enter number 5: 3
Enter number 6: 8
Enter number 7: 15
Enter number 8: 2
Enter number 9: 9
Enter number 10: 14

📊 Results:
Even numbers: [12, 20, 8, 2, 14]
Odd numbers: [5, 7, 3, 15, 9]


## 📚 Key Concepts

- **Modulo Operator (`%`)**: Returns the remainder of division. `number % 2 == 0` means the number is even
- **`range(10)`**: Creates a sequence from 0 to 9 (10 iterations)
- **`.append()`**: Adds an element to the end of a list
- **User Input**: `input()` gets data from the user; `int()` converts it to an integer

## 🛠️ Requirements

- Python 3.x

## ▶️ How to Run

python even_odd_sorter.py


## 🎓 Learning Outcomes

After completing this project, you'll understand:
- How to use `for` loops with `range()`
- How to work with lists in Python
- How conditional statements control program flow
- How to validate even/odd numbers mathematically

## 🌟 Challenge Extensions

Want to level up? Try these modifications:
- Let users choose how many numbers to input
- Add error handling for non-integer inputs
- Calculate and display the sum of each list
- Sort the lists in ascending order before displaying

---

**Happy Coding! 🐍✨**