

import numpy as np

a = np.array([1,2,4,5,7])
b = np.array([4,6,4,8,7])
c = a <= b 
print(a)
print(b)
print(c)
print("There are some True values in array 'c' ",c.any())
print("There are all True values in c",c.all())