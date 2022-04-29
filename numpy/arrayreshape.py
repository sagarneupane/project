
from numpy import * 

a = array([1,2,3,4,5,4,6,7,8,9,10,11,17,18,19,20,21,11])
c = a.reshape(3,3,2)
print(a)
print(c)
b = c.reshape(2,9)
print(b)