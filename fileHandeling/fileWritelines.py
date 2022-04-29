

def writeLines():
    a = {"2","1","b","bear","cow","dog"}
    f = open("fileHandeling/lines.txt",mode="w")
    f.writelines(a)
    # print(n)
    f.close()

# writeLines()

def appendLines():
    a = ["\nSagar","\nSamir","\nSumit","\nsova","\nJanki"]
    f = open("fileHandeling/lines.txt",mode='a')
    f.writelines(a)
    f.close()
    
# appendLines()

def read():
    f = open("fileHandeling/lines.txt",mode='r')
    d1 = f.read(3)
    d2 = f.read(8)
    d3 = f.read(8)
    d4 = f.read(8)
    print(d1,d2,d3,d4)
    f.close()

# read()

def readline():
    f = open("fileHandeling/lines.txt",mode='r')
    d1 = f.readline()
    d2 = f.readline()
    d3 = f.readline()
    print(d1,d2)
    f.close()

def readlines():
    f = open("fileHandeling/lines.txt",mode='r')
    d1 = f.readlines()
    d2 = f.readlines(2)
    for i in d1:
        print(i,end="")
    # print(d1,d2)
    f.close()
readlines()
    

    
    