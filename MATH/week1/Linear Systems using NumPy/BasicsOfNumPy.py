import numpy as np
one_d_array=np.array([10,12])

# Create and print a NumPy array 'a' containing the elements 1, 2, 3.
a = np.array([1, 2, 3])
print(a)


# Create an array with 3 integers, starting from the default integer 0.
b=np.arange(3)
print(b)


# Create an array that starts from the integer 1, ends at 20, incremented by 3.
c=np.arange(1,20,3)
print(c)

lin_spaced_arr=np.linspace(0,100,5)
print(lin_spaced_arr)

lin_spaced_arr=np.linspace(0,100,5,dtype=int)
print(lin_spaced_arr)


c_int = np.arange(1, 20, 3, dtype=int)
print(c_int)

b_float = np.arange(3, dtype=float)
print(b_float)

char_arr = np.array(['Welcome to Math for ML!'])
print(char_arr)
print(char_arr.dtype) # Prints the data type of the array

# Return a new array of shape 3, filled with ones.
ones_arr = np.ones(3)
print(ones_arr)

# Return a new array of shape 3, filled with zeroes.
zeros_arr = np.zeros(3)
print(zeros_arr)

# Return a new array of shape 3, without initializing entries.
empt_arr = np.empty(3)
print(empt_arr)

# Return a new array of shape 3 with random numbers between 0 and 1.
rand_arr = np.random.rand(3)
print(rand_arr)