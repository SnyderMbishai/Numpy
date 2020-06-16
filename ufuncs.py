import numpy as np
from scipy import special

# Arithmetic operations (same as the normal python's)
x = np.arange(4)
print(x)
print(x + 5)
print(x - 5)
print(x * 2)
print(x / 2)
print(x // 2)
print(-x)
print(x ** 2)
print(x % 2)
print(-(0.5*x + 1) ** 2)
print(np.add(x,2))

# Absolute
x = np.array([-2,-1,0,1,2])
print(x)
print(abs(x))
print(np.absolute(x))
print(np.abs(x))

# Complex data
y = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
print(np.abs(y))

""" Trigonometric functions """
theta = np.linspace(0,np.pi,3)
print(theta)
print(np.sin(theta))
print(np.cos(theta))
print(np.tan(theta))

# Inverse Trigonometric functions
i = [-1, 0, 1]
print(i)
print(np.arcsin(i))
print(np.arccos(i))
print(np.arctan(i))

""" Exponents and logarithms """
# Exponentials
e = [1,2,3]
print(e)
print(np.exp(e))
print("2 exp e", np.exp2(e))
print("3 exp e", np.power(3,e))
# Logarithms
l = [1,2,4,10]
print(l)
print(np.log(l))
print(np.log2(l))
print(np.log10(l))

# on very small input: These ones are more precise
x = [0, 0.001, 0.01, 0.1]
print(x)
print(np.expm1(x)) # exp(x-1)
print(np.log1p(x)) # log(1+x)

""" Specialized ufuncs """
# scipy.special
x = [1,5,10]
print(special.gamma(x))
print(special.gammaln(x))
print(special.beta(x,2))


