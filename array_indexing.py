import numpy as np

# One dimension
a1 = np.random.randint(10, size=6)
print(a1)
print(a1[0])
print(a1[-1])

# Multi-dimensional
a2 = np.random.randint(10, size=(3,4))
print(a2)
#accessing individual items
print(a2[0][0])
print(a2[1])
print(a2[1][0])
# numpy arrays have fixed data types, a float will be truncated
a2[0][3] = 8.90
print(a2)

