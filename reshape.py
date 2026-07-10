import numpy as np

a = np.arange(12)

print(a)

b = a.reshape(3, 4) # (rows, cols)
c = a.reshape(2,3,2) # (layers, rows, cols) this is for 3d arrays

print(b)
print(c)

d = np.reshape(a, shape=(3, 4), order='C')