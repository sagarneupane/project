

def readWrite():
    f = open('fileHandeling/fileReadWriteAppend/student.txt',mode='r+')
    d = f.read()
    f.write("Sagar Neupane")
    print(d)
    f.close()
# readWrite()

def writeRead():
    f = open('fileHandeling/fileReadWriteAppend/student.txt',mode='w+')
    f.write("Sagar Neupane")
    print(f.tell())
    f.seek(0)
    d = f.read()
    print(f.tell())
    print(d)
    f.close()
# writeRead()

def appendRead():
    f = open('fileHandeling/fileReadWriteAppend/student.txt',mode='a+')
    a = "Sova Neupane"
    print("your Pointer is at",f.tell())
    f.write(a)
    print("Your Pointer is at",f.tell())
    f.seek(0)
    d = f.read()
    a = len(d) - len(a)
    print(a)
    f.seek(a)
    print("Your Pointer is at",f.tell())
    e = f.read()
    print(f'"{e}" is successfully written to your file')
    print("Your Pointer is at",f.tell())
    f.close()
appendRead()
    