import numpy as np

x = np.arange(6)

y = np.flip(x)

print(y)

x2D = np.arange(6).reshape(2,3)
y2D = np.flip(x2D)
print(y2D)
