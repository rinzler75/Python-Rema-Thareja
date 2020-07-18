class student:
    def __init__(self):
        self.__marks=[]
    def set_data(self,r,n,m1,m2,m3):
        self.__rollno=r
        self.__name=n
        self.__marks.append(m1)
        self.__marks.append(m2)
        self.__marks.append(m3)
    def display(self):
        print("Student Details:")
        print("Roll Number: ",self.__rollno)
        print("Name: ",self.__name)
        print("Marks: ",self.__marks)
        print(" Total Marks: ",sum(self.__marks))
r=int(input("Enter the roll number of the student: "))
n=input("Enter the name of the student: ")
m1=int(input("Enter the marks in first subject: "))
m2=int(input("Enter the marks in second subject: "))
m3=int(input("Enter the marks in third subject: "))
s1=student()
s1.set_data(r,n,m1,m2,m3)
s1.display()
