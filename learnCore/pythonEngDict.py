

def square(n):
    return n*n
n = int(input("Enter the number you want to print square of: "))
print(f'The square of "{n}" is',square(n))

def swap(n,m):
    temp = n
    n = m
    m = temp
    return n,m

print(swap(6, 8))
    