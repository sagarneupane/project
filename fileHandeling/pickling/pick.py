import pickle
import employee as emp

n= int(input("Enter the number of Employee"))

with open("fileHandeling/pickling/emp.dat",mode="wb") as f:
    for i in range(n):
        name = input("Enter the name of Employee: ")
        emp_id = int(input("Enter ID of Employee: "))
        salary = float(input("Enter Salary of Employee: "))
        stu = emp.Employee(name,emp_id,salary)
        pickle.dump(stu,f)
        # pickle.dump(stu2,f)
    
