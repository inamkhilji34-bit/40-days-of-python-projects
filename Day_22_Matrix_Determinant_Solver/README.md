# 📘 Day 22: Matrix Determinant Solver (Hard)

## 🎯 Goal
Learn how to manually calculate **2×2 and 3×3 matrix determinants**, show every step clearly, then verify your answer using **NumPy**.

---

## 📐 What is a Determinant?
A determinant is a **single number** calculated from a square matrix. It's used in linear algebra for things like solving equations, checking if a matrix is invertible, and more.

---

## 🔢 The Formulas

### 2×2 Matrix
| a  b |
| c  d |   →   det = (a×d) - (b×c)


### 3×3 Matrix (Cofactor Expansion along Row 1)
| a  b  c |
| d  e  f |   →   det = a(ei−fh) − b(di−fg) + c(dh−eg)
| g  h  i |

Each term uses a **2×2 sub-determinant** (called a minor).

---

## 🗂️ Project Structure
day22_determinant/
│
├── determinant_solver.py   # Your main solution file
└── README.md               # This file


---

## ✅ What Your Program Should Do

1. **Define** a 2×2 and a 3×3 matrix
2. **Manually calculate** the determinant step by step
3. **Print each sub-determinant** (for 3×3)
4. **Print the final result**
5. **Verify** using `np.linalg.det()`
6. **Compare** both answers

---

## 📦 Requirements
numpy

Install with:
pip install numpy


---

## ▶️ Expected Output Example
```
=== 2x2 Determinant ===
Matrix:
[[2, 3],
 [1, 4]]
Step: (2×4) - (3×1) = 8 - 3 = 5
Manual Result:  5.0
NumPy Result:   5.0
✅ Match!

=== 3x3 Determinant ===
Matrix:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
Sub-det for a=1: (5×9) - (6×8)