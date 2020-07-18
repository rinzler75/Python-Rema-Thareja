class Number:
    def __init__(self,num):
        self.num=num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __oct__(self):
        return oct(self.num)
    def __hex__(self):
        return hex(self.num)
    def __setitem__(self,num):
        self.num=num
N=Number(-14)
print("N IS :",N.display())
print("ABS(N) IS : ",abs(N))
N=abs(N)
print("Converting to the float......",float(N))
print("HEXADECIMAL equivalent........",hex(N))
print("Octal equivalent........",oct(N))