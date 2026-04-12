import numpy as np, math
v1 = np.array(input("Enter vector 1 values separated by spaces: ").split(), dtype=float)
v2 = np.array(input("Enter vector 2 values separated by spaces: ").split(), dtype=float)

if len(v1)== len(v2):
    # dot product manually
    manually = sum(a*b for a,b in zip(v1,v2))
    print(f"Manual dot Product: {manually}")
    # dot product with numpy
    dot = np.dot(v1,v2)
    print(f"Numpy dot product: {dot}")
    m1 = np.linalg.norm(v1)
    m2 = np.linalg.norm(v2)
    if m1 == 0 or m2 ==0:
        print("Cannot compute angle: one or both vectors have zero magnitude.")
    else:
        cosA = max(-1, min(1, dot/(m1*m2))) # clamping 
        angle = math.degrees(math.acos(cosA))
        print(f"Angle: {angle:.2f} degrees")
else:
    print("Dot product is not compatible.")


