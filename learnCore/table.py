

table_of = int(input("Enter the number whose table you want to print"))
table_up_to = int(input("Enter number up_to which you want to print "))
def table(n,m):
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            print(f'{j} x {i:<2} = {i*j:<3}',end=" ")
        print()

table(table_of,table_up_to)