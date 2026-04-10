# Day 16: Matrix Operations 📊

## Overview
Today you'll build a program that takes two matrices from user input, then performs key matrix operations on them using **NumPy**.

---

## What You'll Learn
- Creating matrices from user input
- Matrix addition and multiplication
- Transposing a matrix
- Finding the determinant of a matrix

---

## Key Concepts

### What is a Matrix?
A matrix is a 2D grid of numbers arranged in rows and columns.

| 1  2 |
| 3  4 |


### Operations You'll Perform
| Operation | What it does | NumPy syntax |
|---|---|---|
| **Add** | Adds matching elements | `A + B` |
| **Multiply** | Dot product of matrices | `A @ B` |
| **Transpose** | Flips rows and columns | `A.T` |
| **Determinant** | Scalar value from a matrix | `np.linalg.det(A)` |

---

## Requirements
- Python 3.x
- NumPy library (`pip install numpy`)

---

## How to Run

python matrix_operations.py


---

## Expected Program Flow

Enter rows for Matrix A: 2
Enter cols for Matrix A: 2
Enter element [0][0]: 1
Enter element [0][1]: 2
Enter element [1][0]: 3
Enter element [1][1]: 4

Enter rows for Matrix B: 2
...

Matrix A:
[[1 2]
 [3 4]]

Addition (A + B): ...
Multiplication (A @ B): ...
Transpose of A: ...
Determinant of A: ...


---

## Helpful Hints

import numpy as np

# Create a matrix
A = np.array([[1, 2], [3, 4]])

A + B          # Addition
A @ B          # Multiplication
A.T            # Transpose
np.linalg.det(A)  # Determinant


> ⚠️ **Note:** For multiplication and determinant, both matrices must be **square** and the same size (e.g., 2x2).

---

## Bonus Challenges 🌟
- Handle non-square matrices gracefully
- Let the user choose which operation to perform
- Pretty-print the matrices with labels

---

## You've Got This! 💪
Matrix math sounds scary, but NumPy makes it super simple. Focus on getting the input