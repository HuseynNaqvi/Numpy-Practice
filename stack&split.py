import numpy as np

x  = np.arange(1,25).reshape(2,12)

y = np.hsplit(x, (3,4))

print(y)