import numpy as np
def get_matrix(name):
    while True:
        try:
            rows = int(input(f"Enter {name} rows: "))
            cols = int(input(f"Enter {name} columns: "))
            if rows <= 0 or cols <= 0:
                print("Enter number greater than 0.")
                continue
            break
        except ValueError:
            print("Enter whole numbers.")
    
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = input(f"Row {i+1}: ").split()
                converted = ([float(x) for x in row])
                if len(converted) != cols:
                    print(f"Need exactly {cols} numbers.")
                    continue
                matrix.append(converted)
                break
            except ValueError:
                print("Number only please.")
    return np.array(matrix)

A = get_matrix("Matrix A")
B = get_matrix("Matrix B")

print("\n--- Matrix A ---\n", A)
print("--- Matrix B ---\n", B)

# Addition
if np.shape(A) == np.shape(B):
    print(f"Sum: { A + B}")
else: 
    print("Addition is not possible due to unmatched shapes.")

# Multiplication
try:
    result = A @ B
    print("Multiplication is compatible", result)
    print(f"result shape: {result.shape}")
except ValueError as e:
    print(f"Multiplication is not compatible, {e}")

# Transpose 
print(f"Transpose of Matrix A: {A.T}")
print(f"Transpose of Matrix B: {B.T}")

# Determinant 
for name, M in [("A",A), ("B", B)]:
    if M.shape[0] == M.shape[1]:
        print(f"\nDeterminant of {name}: {round(np.linalg.det(M), 4)}")
    else:
        print(f"\nDeterminant of {name}: not possible — not a square matrix")


