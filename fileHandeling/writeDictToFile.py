

def writeDict():
    import os
    a = {"name":"Sagar Neupane","class":"Bachelor's Final year","symbolno":"074/17032"}
    f = open('fileHandeling/dict.txt',mode='w')
    f.write(f'{a}')
    f.close()
    if os.path.isfile("fileHandeling/dict.txt"):
        print("File Sucessfully Created")
    else:
        print("File not Created")


writeDict()
# print(a)