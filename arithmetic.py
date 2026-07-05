import numpy as np

# Scaler arithmetic

array = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])

#print(array + 1)
#print(array * 3)
#print(array / 2)
#print(array ** 2)

#vectorized Math funcs

radi = np.array([1,2,3])
print(np.pi * radi **2)

# Element-wise arithmetic

array1 = np.array([1,2,3])
array2 = np.array([2,3,4])

print(array1 + array)

# Comparison operators

scores = np.array([50,60,100,80])

print(scores > 90)