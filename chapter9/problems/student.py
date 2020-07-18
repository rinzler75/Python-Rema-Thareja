class student:
    
    roll_nos=[]
    totals=[]
    def __init__(self):
        self.marks=[]
        self.marks.append(int(input("Enter the marks in first subject: ")))
        self.marks.append(int(input("Enter the marks in second subject: ")))
        self.marks.append(int(input("Enter the marks in third subject: ")))
        self.roll_no=input("Enter the roll number")
        student.roll_nos.append(self.roll_no)
        
        student.totals.append(sum(self.marks))
    def display():
        for i in range(len(student.totals)):
            for j in range(0,len(student.totals)-i-1):
                if student.totals[j]<student.totals[j+1]:
                    student.totals[j],student.totals[j+1]=student.totals[j+1],student.totals[j]
                    student.roll_nos[j],student.roll_nos[j+1]=student.roll_nos[j+1],student.roll_nos[j]
        print("Roll No.\t\tTotal marks")
        for i in range(len(student.totals)):
            print(student.roll_nos[i],"\t\t",student.totals[i])
s1=student()
s2=student()
s3=student()
s4=student()
student.display()
    

        
