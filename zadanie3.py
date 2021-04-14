import numpy as np
def tablicaPotegowa(n, m):
     y = np.logspace(start=1,num=m, stop=m, base=n, dtype='int')
     return y
print(tablicaPotegowa(2, 8))