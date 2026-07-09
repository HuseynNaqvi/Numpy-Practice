import numpy as np
import math

array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

x = np.array([7,2,3,9,6])

array2 = (np.empty(8, dtype=np.int64)) # specifying the data type with dtype
xa = np.sort(x) # returns sorted array
xb = np.argsort(x) # returns indices that would sort an array
x.sort() # does not generate a copy, sorts in place

print(xa)
print(xb)