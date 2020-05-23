import numpy as np

#seeding
n = np.random.seed(0)
print(n)

"""
Dimentions
"""
# 1 dimension
x1 = np.random.randint(100, size=5)
print("x1: ", x1)
# 2 dimensions
x2 = np.random.randint(100, size=(3,4))
print("x2: ", x2)
# 3 dimensions
x3 = np.random.randint(100, size=(3,4,5))
print("x3", x3)

# ndim(number of dimensions), shape(size of each dimensions), size(total size of the array), dtype(data type)
# itemsize(size of each element in the array), nbytes(total size of the array)
print(x3.ndim, x3.shape, x3.size, x3.dtype)
print(x3.itemsize, x3.nbytes)

