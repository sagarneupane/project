import numpy as np

arr_in = np.array([4,10,8,15,6])
arr_out = np.array([3,2,9,17,1])

result = np.where(arr_in>arr_out,arr_out,arr_in)

print(result)