
# f = open('student.txt',mode='w')

# f.write("Name: Sagar Neupane\n")
# f.write("Class: Bachelor's Final Sem\n")
# f.write("University: Tribhuvan University")

# f.close()
# print("Write Success")

f = open("student.txt",mode='r',encoding='utf-8')
data = f.read()
print(data)
f.close()


# f = open("student.txt",mode='rb')
# data = f.read()
# print(data)
# f.close()
