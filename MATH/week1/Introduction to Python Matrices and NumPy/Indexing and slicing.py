import numpy as np
from IPython.lib.pretty import Printable

# Select the third element of the array. Remember the counting starts from 0.
a = np.array([1, 2, 3, 4, 5])
print(a[2])

# Select the first element of the array.
print(a[0])

# Indexing on a 2-D array
two_dim = np.array(([1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]))

# Select element number 8 from the 2-D array using indices i, j and two sets of brackets
print(two_dim[2][1])

# Select element number 8 from the 2-D array, this time using i and j indexes in a single
# set of brackets, separated by a comma
print(two_dim[2,1])


#slicing
#The syntax is:

#array[start:end:step]

# If no value is passed to start, it is assumed start = 0,
# if no value is passed to end,
# it is assumed that end = length of array - 1 and if no value is passed to step,
# it is assumed step = 1.

# Slice the array a to get the array [2,3,4]
sliced_arr = a[1:4]
print(sliced_arr)

# Slice the array a to get the array [1,2,3]
sliced_arr = a[:3]
print(sliced_arr)

# Slice the array a to get the array [3,4,5]
sliced_arr = a[2:]
print(sliced_arr)

# Slice the array a to get the array [1,3,5]
sliced_arr = a[::2]
print(sliced_arr)

# Note that a == a[:] == a[::]
print(a)
print(a[:])
print(a[::])

# Slice the two_dim array to get the first two rows
sliced_arr_1 = two_dim[0:2]
print(sliced_arr_1)

# Similarily, slice the two_dim array to get the last two rows
sliced_two_dim_rows = two_dim[1:3]
print(sliced_two_dim_rows)

# This example uses slice notation to get every row, and then pulls the second column.
# this example combines slice notation with the use of multiple indexes
sliced_two_dim_cols = two_dim[:,1]
print(sliced_two_dim_cols)