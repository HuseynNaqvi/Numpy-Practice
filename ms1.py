import numpy as np

# Create a 2D array and reshape it into 3 different valid shapes without checking docs

array = np.arange(6).reshape(2,3)

shape1 = array.reshape(1,6)
shape2 = array.reshape(6,1)
shape3 = array.reshape(1,2,3)

print(shape3)