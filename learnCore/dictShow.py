


# name = input("Enter your Name ") 
# level = input("In which level you studying now? ")
# age = int(input("How old are you? "))

dict_my = {"student1":{"name":"Sagar Neupane","level":"Bachelor's","Age":23},
           "student2":{"name":"Sova Neupane","level":"Not Bachelor's","Age":20},
           "student3":{"name":"Amrita Chapagain","level":"Not Bachelor's","Age":18}
           }

print(dict_my.keys())

for i in dict_my.keys():
    print(i)
    
for i in dict_my:
    print(f'for {i} :::: ' ,end=" ")
    for j in dict_my[i]:
        print(f'{j}=> {dict_my[i][j]}   ',end="  ")
    print()
# print(f'Hello my name is {dict_my["name"]} and I am currently studying {dict_my["level"]} . I am {dict_my["Age"]} years Old')