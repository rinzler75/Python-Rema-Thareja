class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        self.age=0
        self.Marks=0
    def setAge(self,age):
        self.age=age
    def setMarks(self,marks):
        self.Marks=marks
    def Display(self):
        print("Name: %s \n Roll Number: %s \nAge: %s \nMarks: %s"%(self.name,self.roll_no,self.age,self.Marks))
student1=Student("Shivangi",92)
student1.setAge(21)
student1.setMarks(100)
student1.Display()

# Output
# Name: Shivangi
# Roll Number: 92
# Age: 21
# Marks: 100