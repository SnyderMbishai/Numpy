import numpy as np

# One dimensional
x = np.arange(10)
print(x)
print(x[:5])
print(x[5:])
print(x[4:7])
print(x[::-1])

# Multi-dimensional
x1 = np.random.randint(10, size=(3,4))
print(x1)
# Two rows, three columns
print(x1[:2, :3])
# All rows, every other column
print(x1[:3, ::2])
# Reversed 
print(x1[::-1, ::-1])

# Rows and columns
