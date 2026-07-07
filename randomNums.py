import numpy as np

rng = np.random.default_rng()

randomInt = rng.integers(low=1, high =10, size=3)

array = np.array([1,3,4,6,8,9])

rng.shuffle(array)

print(array)

fruits = np.array(["Apple", "Banana", "Mango", "Peach"])

fruit = rng.choice(fruits)

print(fruit)