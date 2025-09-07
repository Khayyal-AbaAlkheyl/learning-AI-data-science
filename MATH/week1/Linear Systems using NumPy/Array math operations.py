import numpy as np


arr_1 = np.array([2, 4, 6])
arr_2 = np.array([1, 3, 5])

# Adding two 1-D arrays
addition = arr_1 + arr_2
print(addition)

# Subtracting two 1-D arrays
subtraction = arr_1 - arr_2
print(subtraction)

# Multiplying two 1-D arrays elementwise
multiplication = arr_1 * arr_2
print(multiplication)


#This concept is called broadcasting, which
# allows you to perform operations specifically
# on arrays of different shapes.
vector = np.array([1, 2])

print(vector * 1.6)