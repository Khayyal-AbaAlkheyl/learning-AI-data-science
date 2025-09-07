import numpy as np

# Create a 2 dimensional array (2-D)
two_dim_arr = np.array([[1,2,3], [4,5,6]])
print(two_dim_arr)

one_d_ar=np.array([1,2,3,4,5,6,])

two_d_ar=np.reshape(one_d_ar,(2,3))

# Dimension of the 2-D array multi_dim_arr
print(two_d_ar.ndim)

# Shape of the 2-D array multi_dim_arr
# Returns shape of 2 rows and 3 columns
print(two_d_ar.shape )

# Shape of the 2-D array multi_dim_arr
# Returns shape of 2 rows and 3 columns
print(two_d_ar.size)