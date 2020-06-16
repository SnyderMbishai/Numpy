import numpy as np

l = np.random.random(100)
print(l)
sm = sum(l)
print(sm)
# numpy's
sm2 = np.sum(l)
print(sm2)

# check time taken
bg_array = np.random.rand(1000000)
# print(%timeit sum(bg_array)) RUN on the console, ipython
# print(%timeit np.sum(bg_array))
