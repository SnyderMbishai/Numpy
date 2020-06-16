import numpy as np

""" out """
x = np.arange(5)
print(x)
y = np.empty(5)
print(y)
np.multiply(x,10,out=y)
print(y)
z = np.zeros(10)
print(z)
np.power(2,x, out=z[::2]) # saves on memory
print(z)

""" Aggegates """
x = np.arange(1,6)
print(x)
print(np.add.reduce(x))
print(np.multiply.reduce(x))
print(np.add.accumulate(x)) # Stores all the results
print(np.multiply.accumulate(x)) ##

# alternatively, use the specific functions -> np.sum, np.prod, np.cumsum, np.cumprod

""" Outer Products """
o = np.arange(1,6)
print(o)
print(np.multiply.outer(x,x))
