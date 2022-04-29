import array

len_arr = int(input("Enter array length. "))

print("What value you want to store inside your Array? ")
print("We have 2 options .\n  1. Press 'a' to insert intger \n2. Press 'b' to insert float \n")

def arary_type():
    val = input("Choose ")
    if val == 'a':
        return 'i'
    elif val == 'b':
        return 'f'
    else:
        print("Enter Valid Options ")
        arary_type()
val = arary_type()

user_array = array.array(val,[])

print("Enter The values ")
if val == 'f':
    for i in range(len_arr):
        a = float(input())
        user_array.append(a)
else:
    for i in range(len_arr):
        a = int(input())
        user_array.append(a)

print(user_array)

