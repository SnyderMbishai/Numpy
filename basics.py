import numpy as np

# Integer array
print("integer array: ", np.array([1,2,3,4]))

# Integer array with datatype
print("integer array float: ", np.array([1,2,3,4], dtype='float32'))

# Multi-dimentional arrays from nested lists
lst = np.array([range(i,i+3) for i in [2,4,6]])
print("multi-dimentional array: {}".format(lst))

"""
creating arrays from scratch
"""
# Zeros array
ar = np.zeros(10, dtype=int)
print("10 zeros: {}".format(ar))

# 3*5 array of ones
ar1 = np.ones((3,5), dtype=float)
print("3*5 ones: {}".format(ar1))

# 3*5 array of 3.14
ar2 = np.full((3,5), 3.14)
print("3*5 3.14: {}".format(ar2))

# Starting at 0, ending at 20, stepping by 2
ar3 = np.arange(0,20,2)
print("0 to 20, stepping 2: %s"%(ar3))

# Array of five values evenly spaced between 0 and 1
ar4 = np.linspace(0,1,5)
print("5, 0 to 1: %s"%(ar4))

#  3x3 array of uniformly distributed values btn 0-1
ar5 = np.random.random((3,3))
print("3*3 btwn 0 - 1: %s"%(ar5))

# 3x3 array of normally distributed random values
# with mean 0 and standard deviation 1
ar6 = np.random.normal(0,1,(3,3))
print("ar6: %s"%(ar6))

# 3x3 array of random integers in the interval [0, 10)
ar7 = np.random.randint(0,10,(3,3))
print("ar7: %s"%(ar7))

# 3x3 identity matrix
ar8 = np.eye(3)
print("Identity matrix: %s"%(ar8))

# Uninitialized array of three integers
ar9 = np.empty(3)
print("ar9: %s"%(ar9))