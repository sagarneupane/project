


def readDict():
    import os
    import json
    import ast
    if os.path.isfile("fileHandeling/dict.txt"):
        f = open("fileHandeling/dict.txt",mode='r')
        a = f.read()
        a = ast.literal_eval(a)
        print(a)
        for i in a:
            print(f'{i} => {a[i]}')
        f.close()
    else:
        print("file Not found")


readDict()