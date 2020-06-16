import numpy as np

bg_array = np.random.rand(1000000)
print(min(bg_array))
print(max(bg_array))

# Using np
print(np.min(bg_array))
print(np.max(bg_array))

# Shorter syntax
bg_array.min()
bg_array.max()
bg_array.sum()

""" Multi dimensional aggregates """

m = np.random.random((3,4))
print(m)
print(m.sum())
print(m.min(axis=0))
print(m.max(axis=1))
