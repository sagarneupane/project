import pickle
import employee as emp


with open("fileHandeling/pickling/emp.dat",mode="rb") as f:
    
    while True:
        try:
            obj = pickle.load(f)
            obj.display()
        except EOFError:
            print("Done")
            break
    