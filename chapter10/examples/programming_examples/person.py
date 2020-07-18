#containership and inheritance mix 

class Person:

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    
    def display(self):
        print("NAME : ",self.name)
        print("AGE : ",self.age)
        print("SEX : ",self.sex)
class Publications:

    def __init__(self,no_RP,no_Books,no_Art):
        self.no_RP=no_RP
        self.no_Books=no_Books
        self.no_Art=no_Art

    def display(self):
        print("No of research papers published: ",self.no_RP)
        print("Numbers of Books Published :",self.no_Books)
        print("Number of articles published : ",self.no_Art)

class Faculty(Person):
    
    def __init__(self,name,age,sex,desig,dept,no_RP,no_Books,no_Art):
        Person.__init__(self,name,age,sex)
        self.desig=desig
        self.dept=dept
        self.Pub=Publications(no_RP,no_Books,no_Art)

    def display(self):
        Person.display(self)
        print("DESIGNATION : ",self.desig)
        print("DEPARTMENT : ",self.dept)
        self.Pub.display()
F=Faculty("Pooja",38,"Female","TIC","Computer Science",22,1,3)
F.display()
