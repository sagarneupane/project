



def readFileLoop():
    f = open("fileHandeling/lines.txt",mode='r')
    d = f.read()
    my_listD = []
    print(len(d))
    for i in range(0,len(d),5):
        f.seek(i)
        # l = f.tell()
        myD = f.read(5)
        my_listD.append(myD)
    print(my_listD)
    f.close()
    
readFileLoop()
    