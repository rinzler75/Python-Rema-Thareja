class student:
    def detail(self):
        #if you have put init class over here then as derived class doesnt have init when the object 
        #creation takes place then the control will come over here
        #same thing will be executed twice
        self.roll_no=input("Enter the roll no of the student: ")
        self.name=input("Enter the name of the student: ")

class fees(student):
    fees=75000
    def submit_fees(self):
        student.detail(self)
        submission=int(input("Enter the fees needs to be submitted : "))
        self.submission=submission
        self.remaning=fees.fees-submission
        if submission==fees.fees:
            print("*****RECIEPT******")
            self.reciept()
        else:
            print("Amount is low!!! ")
            print("Please pay the remaining amount under extended time of 2 months!!!")
            self.reciept()
            
   
    def reciept(self):
        
        print("Roll no: ",self.roll_no)
        print("Name : ",self.name)
        print("Fees deposited : ",self.submission)
        print("Remaining amount: ",self.remaning)

f=fees()
f.submit_fees()
