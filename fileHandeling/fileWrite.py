


f = open("fileHandeling/readme.txt",'w')
f.write("helllo My name is Sagar neupane")
f.close()

f = open("fileHandeling/readme.txt",mode='r')
a = f.read() 
print(a)
# f.write("2. This is written afterwards\n")
# b = f.read()
# print(b)
f.close()