import numpy as np

a = np.arange(12)

print(a)

b = a.reshape(3, 4) # (rows, cols)
c = a.reshape(2,3,2) # (layers, rows, cols) this is for 3d arrays

print(b)
print(c)

d = np.reshape(a, shape=(3, 4), order='C')

 # Transposing an array

y = np.arange(6).reshape(2,3)
y1 = y.T

print(y1)

#Flattening and Reshaping

x = np.arange(12).reshape(3,1,4)
xflat = x.flatten() # does not affect original array
xravel = x.ravel() #  can affect the original (view, when possible).

print(xflat)