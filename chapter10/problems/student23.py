class student:
    def __init__(self):
        self.tests=[]
        self.activities=[]
        self.name=input("Enter the name of the student: ")
        self.sports=int(input("Enter the marks obtained in sports: "))
        for i in range(3):
            print("Enter the marks in activity ",i+1,":")
            self.activities.append(int(input()))
        for i in range(3):
            print("Enter the marks in test of sub",i+1,":")
            self.tests.append(int(input()))
    
    def evaluate(self):
        
        print("Name : ",self.name)
        print("Marks obtained in Activities : ",sum(self.activities))
        print("Marks obtained in tests: ",sum(self.tests))
        print("Total Marks obtained: ",sum(self.activities)+sum(self.tests))
s1=student()
s1.evaluate()
    
        