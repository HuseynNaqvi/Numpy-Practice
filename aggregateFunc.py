import numpy as np

array1 = np.array([[1,2,3,4,5],
                   [6,7,8,9,10]])

print("sum:", np.sum(array1))
print("mean:", np.mean(array1))
print("standard deviation:", np.std(array1))
print("variance:", np.var(array1))
print("minimum value:", np.min(array1))
print("maximum value:", np.max(array1))
print("position of min value:", np.argmin(array1))
print("position of max value:", np.argmax(array1))
print("sum of all rows:", np.sum(array1, axis=0))
print("sum of all cols:", np.sum(array1, axis=1))
