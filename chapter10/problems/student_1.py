class student:
    names=[]
    roll_no=[]
    total_marks=[]
    def detail(self):
        for i in range(5):
            student.names.append(input("Enter the name of the student: "))
            student.roll_no.append(input("Enter the roll no of the student: "))
            self.sub1=int(input("Enter the marks of student in sub1: "))
            self.sub2=int(input("Enter the marks of student in sub2: "))
            self.sub3=int(input("Enter the marks of student in sub3: "))
            student.total_marks.append(self.sub1+self.sub2+self.sub3)
        for i in range(5):
            for j in range(0, 5-i-1):
                if student.total_marks[j] > student.total_marks[j+1] :
                    student.total_marks[j], student.total_marks[j+1] = student.total_marks[j+1],student.total_marks[j]
                    student.roll_no[j],student.roll_no[j+1]=student.roll_no[j+1],student.roll_no[j]
                    student.names[j],student.names[j+1]=student.names[j+1],student.names[j]
class Toppers(student):
    def print_det(self):
        for i in range(3):
            print("\n\n****TOPPER ",i+1,"******")
            print("Name: ",student.names[i])
            print("Roll No.: ",student.roll_no[i])
            print("Marks : ",student.total_marks[i])
s=Toppers()
s.detail()
s.print_det()       


