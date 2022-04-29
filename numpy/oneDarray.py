

import numpy as np

my_array = np.array([1,2,4,8],dtype=str)

length = len(my_array)
i=0
while(i<length):
    print(my_array[i])
    i=i+1
print("From for Loop")
for i in my_array:
    print(i)

