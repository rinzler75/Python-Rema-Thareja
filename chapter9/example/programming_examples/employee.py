class Employee:
    empCount=0
    def __init__(self,name,desig,salary):
        self.name=name
        self.desig=desig
        self.salary=salary
        Employee.empCount+=1 #counts the number of employee or the number of objects made of the class 
        #EMPLOYEE
    def displayCount(self):
        print("There are %d employees"%Employee.empCount)
    def displayDetails(self):
        print("Name : ",self.name,"Designation : ",self.desig,"Salary : ",self.salary)
e1=Employee("Farhan","Manager",100000)
e1.displayCount()
e1.displayDetails()