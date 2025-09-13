import numpy as np
import w2_unittest

A=np.array([
    [2,-1,1,1],
    [1,2,-1,-1],
    [-1,2,2,2],
    [1,-1,2,1]
],dtype=float)
b=np.array([6,3,14,8],dtype=float)

d=np.linalg.det(A)

x=np.linalg.solve(A,b)

print(f"The Determinant of the matrix A is: {d:.2f}")

print (f"The solution vector is:{x}")

w2_unittest.test_det_and_solution_scipy(d,x)
