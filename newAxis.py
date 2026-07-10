import numpy as np

x = np.arange(6)
x2 = x[np.newaxis, :] # row vector
x3 = x[:, np.newaxis] # col vector

print(x3)
print(x3.shape)