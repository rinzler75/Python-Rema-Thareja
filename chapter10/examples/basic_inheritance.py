class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("NAME: ",self.name)
        print("AGE: ",self.age)
class Teacher(Person): #inheritance syntax
     #method overided here
    def __init__(self,name,age,exp,r_area):
        Person.__init__(self,name,age)
        self.exp=exp
        self.r_area=r_area
    def displayData(self):
        Person.display(self)
        print("EXPERIENCE : ",self.exp)
        print("RESEARCH AREA : ",self.r_area)
class Student(Person):
    #method overided that's y init needs to be called again
    def __init__(self,name,age,course,marks):
        Person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displayData(self):
        Person.display(self)
        print("COURSE: ",self.course)
        print("MARKS: ",self.marks)

print("************TEACHER**************")
T=Teacher("JAYA",43,20,"Recommended Systems")
T.displayData()
print("***************STUDENT*************")
S=Student("Mani","20","B Tech",78)
S.displayData()

#isinstance and issubclass methods 
print("T is a Teacher : ",isinstance(T,Teacher))
print("T is a person : ",isinstance(T,Person))
print("T is an integer: ",isinstance(T,int))
print("T is an object: ", isinstance(T,object))
print(" Person is a subclass of Teacher : ",issubclass(Person,Teacher))
print("Teacher is a subclass of Person: ",issubclass(Teacher,Person))
print(" Boolean is a subclass of int : ",issubclass(bool,int))