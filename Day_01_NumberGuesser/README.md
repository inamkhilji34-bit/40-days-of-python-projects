# 🎯 Number Guesser Game

A fun command-line game where you try to guess a randomly generated number between 1 and 100. The computer gives you hints to help you find the answer!

## 📋 Project Description

This is a beginner-friendly Python project that helps you practice:
- Using the `random` module
- Working with loops (`while` loops)
- Getting user input with `input()`
- Conditional statements (`if`, `elif`, `else`)
- Basic game logic

## 🎮 How to Play

1. The computer picks a random number between 1 and 100
2. You make a guess
3. The computer tells you if your guess is:
   - **Too High** 📈
   - **Too Low** 📉
   - **Correct!** 🎉
4. Keep guessing until you find the right number
5. The game tells you how many attempts it took!

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your computer
- A terminal or command prompt

### Installation

1. Clone or download this project
2. Navigate to the project directory
3. Run the game:

python number_guesser.py


## 💻 Code Example

Here's what the main game logic looks like:

import random

# Generate random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guesser Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too Low! Try again.")
    elif guess > secret_number:
        print("Too High! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        break


## 🎯 Learning Objectives

By completing this project, you'll learn:

- ✅ How to generate random numbers with `random.randint()`
- ✅ How to create game loops with `while True`
- ✅ How to break out of loops with `break`
- ✅ How to convert user input to integers with `int()`
- ✅ How to use comparison operators (`<`, `>`, `==`)
- ✅ How to keep track of game state with variables

## 🔧 Possible Enhancements

Want to make the game more interesting? Try adding:

1. **Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-500)
2. **Limited Attempts**: Give the player only 7 tries
3. **Play Again**: Ask if they want to play another round
4. **High Score**: Keep track of the fewest attempts
5. **Input Validation**: Handle non-numeric inputs gracefully

## 📚 Key Concepts

### Random Module
import random
number = random.randint(1, 100)  # Random integer from 1 to 100 (inclusive)


### While Loop with Break
while True:
    # Game logic here
    if condition_met:
        break  # Exit the loop


### Counter Variable
attempts = 0
attempts += 1  # Increment by 1 each time


## 🐛 Common Mistakes to Avoid

1. **Forgetting to import random**: Always start with `import random`
2. **Not converting input**: Use `int(input())` not just `input()`
3. **Infinite loops**: Make sure you have a `break` condition
4. **Off-by