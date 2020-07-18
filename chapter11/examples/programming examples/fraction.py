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
        self.num=int(input("Enter the numerator: "))
        self.deno=int(input("Enter the denominator: "))
    def simplify(self):
        common_divisor=GCD(self.num,self.deno)
        self.num//=common_divisor
        self.deno//=common_divisor
    def __add__(self,F):
        Temp=Fraction()
        Temp.num=(self.num*F.deno)+(self.deno*F.num)
        Temp.deno=self.deno*F.deno
        return Temp
    def display(self):
        self.simplify()
        print(self.num,"/",self.deno)
F1=Fraction()
F1.get()
F2=Fraction()
F2.get()
F3=Fraction()
F3=F2+F1
print("The resultant fraction is :")
F3.display()