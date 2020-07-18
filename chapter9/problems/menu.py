from fractions import Fraction
class simplify():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    
ch=0
while ch!=4:
    print('''*********MENU*********
             1. READ
             2. DISPLAY
             3. SIMPLIFY 
             4. EXIT''')
    ch=int(input("Enter your choice: "))
    if ch==1:
        num1=int(input("Enter the numerator of the first number: "))
        den1=int(input("Enter the denomenator of the first number: "))
        num2=int(input("Enter the numerator of the second number: "))
        den2=int(input("Enter the denomenator of the second number: "))
        s=simplify(num1/den1,num2/den2)
    elif ch==2:
        print("The first number is : "+str(Fraction(s.a)))
        print("The second number is: "+str(Fraction(s.b)))
    elif ch==3:
        print("1.ADD \n 2.SUBTRACT")
        choice=int(input("Enter the operation: "))
        if choice==1:
            print("The result is :  "+str(Fraction(s.add())))
        elif choice==2:
            print("The result is : "+str(Fraction(s.subtract())))