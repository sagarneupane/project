

import array
import sys

my_arr = array.array('i',[2,45,68,9,6])
size_occupied_by_array = sys.getsizeof(my_arr)
print(size_occupied_by_array,"bytes")
array_size = len(my_arr)

print(my_arr)
for i in range(array_size):
    print(my_arr[i])

my_arr.remove(45)

my_arr.pop()
print(my_arr)