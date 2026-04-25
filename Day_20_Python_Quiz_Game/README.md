# Day 20: Python Quiz Game 🐍

## Overview
A command-line quiz game that tests Python knowledge with 10 questions, tracks your score, and awards a letter grade at the end.

---

## Features
- 10 Python trivia questions
- Score tracking throughout the game
- Reveals the correct answer if you guess wrong
- Letter grade at the end (A, B, C, D, or F)

---

## How to Run

python quiz_game.py


---

## How to Play
1. Run the program
2. Read each question carefully
3. Type your answer and press Enter
4. See if you're right — or learn the correct answer
5. Get your final score and letter grade

---

## Example Output

Question 1: What keyword is used to define a function in Python?
Your answer: def
✅ Correct!

Question 2: What data type is the result of 10 / 2 in Python 3?
Your answer: int
❌ Wrong! The correct answer is: float

...

Quiz Complete!
You scored 80 out of 100
Grade: B


---

## Grade Scale

| Score  | Grade |
|--------|-------|
| 90–100 |   A   |
| 80-89  |   B   |
| 70-79  |   C   |
| 60-69  |   D   |
| 0-59   |   F   |

---

## Key Concepts Used
- Lists of dictionaries (`questions = [{...}, {...}]`)
- `for` loops
- `input().strip().lower()` for clean answer comparison
- Conditionals (`if/else`)
- f-strings for output
- Score counter variable

---

## File Structure

day20/
│
├── quiz_game.py   # Main quiz program
└── README.md      # This file


---

## Requirements
- Python 3.x
- No external libraries needed

---

*Day 20 of 40 Days of Python* 🚀