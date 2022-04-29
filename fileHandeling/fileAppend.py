
import os

if os.path.isfile("fileHandeling/readme.txt"):
    

    f = open('fileHandeling/readme.txt',mode='a')

    f.write("\nHello world and this is other next next")

    f.close()
else:
    print("File not Present")
    
if os.path.isfile("internship/another"):
    f = open("internship/another",mode="rb")
    a = f.read()
    print(a)
else:
    print("file not present")