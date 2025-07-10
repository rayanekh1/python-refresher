import numpy as np

# messing with vectors
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vector a:", a)
print("Vector b:", b)

print("Sum:", a + b)
print("Diff:", a - b)

# matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

print("A + B:\n", A + B)
print("A - B:\n", A - B)

# dot product
dot = a @ b
print("\nDot product:", dot)

# matrix mult (for some reason they use 2x3 and 3x2 here?)
A_big = np.array([[1, 2, 3], [4, 5, 6]])
B_big = np.array([[7, 8], [9, 10], [11, 12]])

product = A_big @ B_big
print("\nMatrix product:\n", product)

# magnitude
v = np.array([1, 1, 2])
print("\nMagnitude of", v, ":", np.linalg.norm(v))

# transpose
A_trans = np.array([[1, 2], [3, 4]])
print("\nOriginal:\n", A_trans)
print("Transpose:\n", A_trans.T)
