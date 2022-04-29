
import numpy as np


array_zeros = np.zeros(5,dtype=bool,order='C')

length = len(array_zeros)
i=0
while i<length:
    print(array_zeros[i])
    i+=1
    
print("********** From For Loop ********")

for i in range(length):
    print(array_zeros[i])