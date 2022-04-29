
import array

len_arr = int(input("Enter How many Elements You want to put inside Array? "))

user_array = array.array('i',[])

print("Enter the Elements: \n Note: They Must be Integer:")
for i in range(len_arr):
    elem = int(input())
    user_array.append(elem)

i=0
while(i<len_arr):
    print(f'Your {i+1} element is',user_array[i])
    i=i+1
