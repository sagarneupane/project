

a = input()

def function(a):
    mySet = []
    mySet_lost = {"",}
    for i in range(0,len(a)-1,2):
        if int(a[i]) > int(a[i+1]):
            mySet.append(a[i])
            # print(a[i])
        elif int(a[i]) == int(a[i+1]):
            mySet_lost.add("Boom Lost")
            # print("Boom Lost")
        else:
            mySet.append(a[i+1])
            # print(a[i+1])
    if len(mySet)!=0:
        elem = "".join(mySet)   
        return elem
    else:
       return "Game Over"
    
b = function(a)
print(b)