
def checkPrimeComposite(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    return count

a = checkPrimeComposite(21)
if a==0:
    print("The number is Prime")
else:
    print("The number is composite")

def printPrime(n):
    prime_list = []

    for i in range(2,n+1):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            prime_list.append(i)
        
    return prime_list

b = printPrime(28)

print(b)


def printComposite(n):
    composite_list = []
    for i in range(2,n+1):
        count = 0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count>=1:
            composite_list.append(i)
    return composite_list


c = printComposite(20)
print(c)
            