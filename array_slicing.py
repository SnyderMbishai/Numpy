import numpy as np

# """ One dimensional """
# x = np.arange(10)
# print(x)
# print(x[:5])
# print(x[5:])
# print(x[4:7])
# print(x[::-1])

# """ Multi-dimensional """

x1 = np.random.randint(10, size=(3,4))
# print(x1)
# # Two rows, three columns
# print(x1[:2, :3])
# # All rows, every other column
# print(x1[:3, ::2])
# # Reversed 
# print(x1[::-1, ::-1])

# """ Rows and columns """

# # First Column
# print(x1[:,0])
# # First row
# print(x1[0,:])
# # : can be ommited when accessing rows
# print(x1[0])

""" Subarrays(no copy) """
print("subarrays")
print(x1)
# 2 by 2 from x1
sub_x1 = x1[:2, :2]
print(sub_x1)
# Changing the sub changes the x1. It's helpful when working with large datasets are you can work with bits of it at a given time
sub_x1[0,0] = 5
print(x1)

""" Copies of arrays """
print("copies")
sub_x1_copy = x1[:2,:2].copy()
print(x1)
print(sub_x1_copy)
sub_x1_copy[0,0] = 88
print(sub_x1_copy)
print(x1)
