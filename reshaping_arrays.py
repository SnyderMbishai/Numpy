import numpy as np

# Create array
arr = np.arange(1,10)
print(arr)

# Turn 3 * 3
grid = arr.reshape(3,3)
print(grid)

# Reshape of array -> row vector
arr1 = np.array([1,2,3])
arr1.reshape(1,3)
print(arr1)

# # New axis -> row vector
arr1[np.newaxis, :]
print(arr1)

# Reshape -> column vector
arr1.reshape(3,1)
print(arr1)

# New axis -> column vector
arr1[:, np.newaxis]
print(arr1)
