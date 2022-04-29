


from numpy import *

user_array = array([[1,2,3,4],[5,6,7,8]] , dtype=int)


for i in range(0,len(user_array)):
    for j in range(0,len(user_array[i])):
        print(f'{i}{j} array=>',user_array[i][j])
        

for i in user_array:
    for j in i:
        print(j,end=" ")
    print()
   
print("using While Loop********* ")
i = 0
while i<len(user_array):
    j=0
    while j<len(user_array[i]):
        print(user_array[i][j],end=" ")
        j+=1
    print()
    i+=1
    