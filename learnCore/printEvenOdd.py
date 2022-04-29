
def showOdd(n):
    list_odd = []
    
    for i in range(1,n+1):
        if i%2!=0:
            list_odd.append(i)
    return list_odd

b = showOdd(20)
print(b)



def showEven(n):
    list_even = []
    for i in range(1,n+1):
        if i%2==0:
            list_even.append(i)
    return list_even

a = showEven(10)
print(a)