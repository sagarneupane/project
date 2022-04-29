


def convert(n):
    return bin(n)

a = convert(15)
print(a)

from array import *

array_my = array('i',[4,45,58,58])
largest = 0
for i in array_my:
    if i > largest:
        largest = i
print(largest)