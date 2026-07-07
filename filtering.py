import numpy as np

ages = np.array([[15, 17 , 21, 18, 19, 54],
                  [21, 24, 29, 13, 16, 55]])

teenagers = ages[ages<20]
adults = ages[(ages>=18) & (ages < 50)]
seniors = ages[ages>50]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

onlyAdults = np.where(ages >= 18, ages, 0)

print(onlyAdults)