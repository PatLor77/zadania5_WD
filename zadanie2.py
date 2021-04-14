import numpy as np
def powerOf2Array(n : int):
     y = 2**np.mgrid[1:n+1, 1:n+1]
     return y
print(powerOf2Array(20))