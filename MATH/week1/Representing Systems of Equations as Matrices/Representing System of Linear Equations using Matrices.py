import numpy as np
import matplotlib.pyplot as plt

A = np.array([
        [-1, 3],
        [3, 2]
    ], dtype=np.dtype(float))

b = np.array([7, 1], dtype=np.dtype(float))

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {A.shape}")
print(f"Shape of b: {b.shape}")

# print(f"Shape of A: {np.shape(A)}")
# print(f"Shape of A: {np.shape(b)}")

x = np.linalg.solve(A, b)

print(f"Solution: {x}")

d = np.linalg.det(A)

print(f"Determinant of matrix A: {d:.2f}")