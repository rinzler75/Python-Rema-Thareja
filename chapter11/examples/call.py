class Mult:
    def __init__(self,num):
        self.num=num
    def __call__(self,o):
        return self.num*o
x=Mult(10)
print(x(5))#using object like a function