class complex:
    def __init__(self):
        self.real=0
        self.imag=0
    def setValue(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,C):
        Temp=complex()
        Temp.real=self.real+C.real
        Temp.imag=self.imag+C.real
        return Temp
    def display(self):
        print("(",self.real,"+",self.imag,"i)")

C1=complex()
C1.setValue(1,2)
C2=complex()
C2.setValue(3,4)
C3=complex()
C3=C1+C2
print("RESULT= ")
C3.display()

