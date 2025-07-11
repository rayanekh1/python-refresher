import numpy as np

# Q1: vector math
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(f"sum: {vec1 + vec2}")
print(f"diff: {vec1 - vec2}")

# Q2: matrix addition + subtraction
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
print(f"matrix sum:\n{mat1 + mat2}")
print(f"matrix diff:\n{mat1 - mat2}")

# Q3: dot product
print(f"dot: {np.dot(vec1, vec2)}")

# Q4: matrix mult
m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
print(f"product:\n{np.dot(m1, m2)}")

# Q5: magnitude
v = np.array([1, 1, 2])
print(f"magnitude: {np.linalg.norm(v)}")

# Q6: transpose
print(f"transpose:\n{mat1.T}")
