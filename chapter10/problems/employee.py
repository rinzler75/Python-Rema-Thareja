class employee:
    def __init__(self):
        self.empl_names=[]
        self.empl_age=[]
        self.empl_number=[]
        for i in range(3):
            print("Enter the name of employee",i+1," under manager(",self.name,"):")
            self.empl_names.append(input())
            print("Enter the age of employee: ")
            self.empl_age.append(input())
            print("Enter the Employee number of employee: ")
            self.empl_number.append(input())
    def display(self):
        print("%-20s %-20s %-20s"%("Name","Number","Age"))
        for i in range(3):
            print("%-20s %-20s %-20s"%(self.empl_names[i],self.empl_number[i],self.empl_age[i]))

class manager(employee):
    def __init__(self):
        self.name=input("Enter the manager name: ")
        self.age=input("Enter the age of the manager: ")
        self.number=input("Enter the number of the manager: ")
        employee.__init__(self)
    def display_data(self):
        print("-----Manager Detail------")
        print("Name: ",self.name)
        print("Number: ",self.number)
        print("Age: ",self.age)
        print("-------Employees under him--------")
        self.display()

m1=manager()
m1.display_data()

