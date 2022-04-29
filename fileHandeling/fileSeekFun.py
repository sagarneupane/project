

def tellFile():
    f = open("fileHandeling/lines.txt",mode='r')
    d = f.read(5)
    
    print(f.tell())
    e = f.read(5)
    print(e)
    print(f.tell())
    print(d)
    f.close()
    
# tellFile()

def seekFile():
    f = open("fileHandeling/lines.txt",mode='r')
    d = f.read(4)
    print(d)
    f.seek(4+2)
    e = f.read(4)
    
    # print(d)
    print(e)
    f.close()
    
seekFile()
    
