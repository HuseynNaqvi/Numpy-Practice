import numpy as np

x = np.array([[12,11,15],
              [21,25,20],
              [18,27,16]])

y = np.sort(x) # sorts along the row by default
yy = np.sort(x, axis= 0) # sorts along cols
yarg = np.argsort(x)
yyarg = np.argsort(x, axis=0)
x.sort()
x.sort(axis=0)