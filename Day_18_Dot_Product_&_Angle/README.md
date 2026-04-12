# Day 18: Dot Product and Angle Between Vectors 🧮

## What You'll Learn
- What a dot product is and how to compute it manually
- How to use NumPy to do the same thing faster
- How to find the angle between two vectors in degrees

---

## 📐 The Math (Don't worry, it's simpler than it looks!)

### Dot Product
Multiply matching elements, then add them all up:

a = [1, 2, 3]
b = [4, 5, 6]

dot = (1×4) + (2×5) + (3×6) = 4 + 10 + 18 = 32


### Magnitude (length of a vector)
|a| = √(1² + 2² + 3²) = √14


### Angle Between Vectors
cos(θ) = dot(a, b) / (|a| × |b|)
θ = arccos(result) → convert to degrees


---

## 📁 File Structure

day18_dot_product/
│
├── dot_product.py       # Your main solution file
├── README.md            # This file
└── test_dot_product.py  # Optional: test your work


---

## ✅ Your Task

Inside `dot_product.py`, write code that:

1. **Manually computes** the dot product using a loop or list comprehension
2. **Computes the magnitude** of each vector manually
3. **Calculates the angle** between the two vectors in degrees
4. **Repeats steps 1–3 using NumPy** (`np.dot()` and `np.linalg.norm()`)
5. **Prints both results** and confirms they match

---

## 💡 Key Hints

import math
import numpy as np

# Angle formula
angle = math.degrees(math.acos(dot / (mag_a * mag_b)))

# NumPy magnitude
mag = np.linalg.norm(vector)


---

## 🧪 Example Output

```
=== Manual Calculation ===
Dot Product: 32
Magnitude of a: 3.7417
Magnitude of b: 8.7750
Angle: 12.9332 degrees

=== NumPy Calculation ===
Dot Product: 32
Magnitude of a: 3.7417
Magnitude of b: 8.7750