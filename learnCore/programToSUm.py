

def addSum(numbers_to_add):
    
    n= numbers_to_add
    numbers = []
    print("Enter the numbers you want to add")
    for i in range(0,n):
        num = int(input(""))
        numbers.append(num)
    sumnum = 0
    for i in range(0,n):
        sumnum += numbers[i]
    
    return sumnum

n = int(input("Enter how Many Numbers you want to Add.. "))

print(addSum(n))
    
        