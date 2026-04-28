import numpy as np
rows = int(input("rows: "))
cols = int(input("cols: "))
matrix = [[int(input(f"[{i}][{j}]: ")) for j in range(cols)]for i in range (rows)]
print(matrix)
if rows != cols:
    print("Determinant only exist for square matrix.")
elif rows == 2 and cols == 2:
    a,b = matrix[0][0],matrix[0][1]
    c,d = matrix[1][0],matrix[1][1]
    det = (a*d) - (b*c)
    print(f"Manual Determinant: {det}")
    np_det = np.linalg.det(matrix)
    print(f"Numpy Confirms: {round(np_det,2)}")
elif rows == 3 and cols == 3:
    a,b,c = matrix[0][0], matrix[0][1], matrix[0][2]
    d,e,f = matrix[1][0], matrix[1][1], matrix[1][2]
    g,h,i = matrix[2][0], matrix[2][1], matrix[2][2]
    x = a*(e*i-f*h)
    y = b*(d*i - f*g)
    z = c*(d*h - e*g)
    print(f"Cofactor term 1: {x}")
    print(f"Cofactor term 2: {y}")
    print(f"Cofactor term 3: {z}")
    det = x - y + z
    print(f"Manual Determinant: {det}")
    np_det = np.linalg.det(matrix)
    print(f"Numpy confirms: {round(np_det,2)}")
else:
    print("The matrix size should be 2*2 or 3*3.")
