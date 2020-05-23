import numpy as np

# Concatenate two arrays
a = np.array([1,2,3])
b = np.array([3,2,1])
np.concatenate([a,b])
print(np.concatenate([a,b]))

# Concatenate more than two arrays
c = np.array([7,7,7])
print(np.concatenate([a,b,c]))

# Multi-dimensional
grid = np.array([
    [1,2,3],
    [4,5,6]
    ])
print(grid)

np.concatenate([grid,grid]) # along first axis
print(np.concatenate([grid,grid]))

np.concatenate([grid,grid], axis=1) # along second axis
print(np.concatenate([grid,grid], axis=1))

""" mixed dimensions """
mx1 = np.array([1,2,3])
mx2 = np.array([
    [9,8,7],
    [6,5,4]
])

# Vertical stack
v = np.vstack([mx1, mx2])
print(v)

# Horizontal stack
mx3 = np.array([
    [88],
    [77]
])
h = np.hstack([mx2,mx3])
print(h)

"""
Splitting
"""
# np.split, np.vsplit, np.hsplit
x = [1, 2, 3, 99, 99, 3, 2, 1]
x1,x2,x3 = np.split(x,(3,5))
print(x1,x2,x3)

s = np.arange(16).reshape(4,4)
print(s)

upper, lower = np.vsplit(s,[2])
print(upper, lower)

left,right = np.hsplit(s,[2])
print(left,right)
