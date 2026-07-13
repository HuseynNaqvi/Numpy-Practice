import numpy as np

a = np.array([1,1,2,2,4,5,8,8,8,9,0,0])

b, c = np.unique(a, return_counts=True)

print(b)
print(c)

# to print this asa dict

print(dict(zip(b.tolist(),c.tolist())))