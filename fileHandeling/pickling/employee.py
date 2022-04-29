



class Employee(object):
    def __init__(self,name,eid,salary):
        self.name = name
        self.eid = eid
        self.salary = salary
    
    def display(self):
        print(f'Name of Employee: {self.name} Id of Employee: {self.eid} Salary of Employee: {self.salary}')
        