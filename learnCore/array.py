
import array

my_array = array.array('i',[115,120,304,44])

for i in range(len(my_array)):
    print(my_array[i])

i=1
while(i<5):
    print(i)
    i=i+1

i=0
length = len(my_array)
while(i<length):
    print(f'Array Element {i+1}',my_array[i])
    i=i+1
    