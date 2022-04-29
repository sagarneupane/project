

def findNumberPower(a):
    list_a = []
    
    for i in str(a):
        list_a.append(i)
    num = 0
    for i in range(len(list_a)):
        if i == len(list_a)-1:
            num = num + pow(int(list_a[i]),int(list_a[i-len(list_a)+1]))
        else:
            num =  num + pow(int(list_a[i]),int(list_a[i+1]))
    return num
    
a  = int(input())

b = findNumberPower(a)
print(b)