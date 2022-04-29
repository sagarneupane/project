
str1 = "oleelo"
str2 = str1.lower()

def string_value(strv):
    str3 = ""
    for i in range(len(strv)-1,-1,-1):
       str3 = str3 + strv[i]
    if str3 == strv:
        return "The string is plaindrome"
    else:
        return "The string is not palindrome"
print(string_value(str2))

v_list = ['a','e','i','o','u']

count=0
str_set = {"",}
str_vow = {"",}
for i in str2:
    str_set.add(i)
print(str_set)
for i in str_set:
    for j in v_list:
        if i==j:
            count+=1
            str_vow.add(j)

          
print(f'{count} vowels are present in {str2} and they are')
for v in str_vow:
    print(f'{v}',end=",")
print()
count=0
for i in str1:
    for j in v_list:
        if i == j:
            count+=1

print(f'{count} times the vowels are repeated')