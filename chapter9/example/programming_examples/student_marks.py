class Students:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def enterMarks(self):
        for i in range(3):
            #new way of taking input
            m=int(input("Enter the marks of %s in subject %d :"%(self.name,i+1)))
            self.marks.append(m)
    def display(self):
        print(self.name,"got",self.marks)
s1=Students('Merlin')
s1.enterMarks()
s2=Students('Navnit')
s2.enterMarks()
s1.display()
s2.display()

        