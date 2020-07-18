import sys

def GCD(num,deno):
    if(deno==0):
        return num
    else:
        return GCD(deno,int(num%deno))
class Fraction:
    def __init__(self):
        self.num=0
        self.deno=1
    def get(self):
        try:
            self.num=int(input("Enter the numerator: "))
            self.deno=int(input("Enter the denominator: "))
            if self.deno==0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Denominator of a fraction can't be zero")
            sys.exit(0)
            
    def simplify(self):
        common_divisor=GCD(self.num,self.deno)
        self.num//=common_divisor
        self.deno//=common_divisor
    def __truediv__(self,D):
        self.simplify()
        D.simplify()
        Temp=Fraction()
        Temp.num=self.num*D.deno
        Temp.deno=self.deno*D.num
        Temp.simplify()
        return Temp
    def display(self):
        self.simplify()
        print(self.num,"/",self.deno)
F1=Fraction()
F1.get()
F2=Fraction()
F2.get()
F3=Fraction()
F1/=F2
print("The resultant fraction is :")
F1.display()