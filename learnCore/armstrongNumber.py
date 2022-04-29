

def checkArmstrong(n):
    number = 0
    for i in n:
        number += int(i) * int(i) * int(i)
    return number
n = "0"
number = checkArmstrong(n)
if number == int(n):
    print("The number is armstrong")
else:
    print("The number is not armstrong")
        
        