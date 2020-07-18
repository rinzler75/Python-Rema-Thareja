class ABC():
    class_var=0 #CLASS VARIABLE 
    def __init__(self,var):
        ABC.class_var+=1 #ACCES METHODS
        self.var=var  #object variable
        print("The object value is :",var)
        print("The value of the class variable is: ",ABC.class_var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)

#--------------------------------
class Number:
    even=0 #every object even part will have 0 
    def check(self,num):
        if num%2==0:
            self.even=1
    def Even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=Number()
n.Even_odd(21)

#----------------------------with mutables
class number:
    even=[]
    odd=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            number.even.append(num)
        else:
            number.odd.append(num)
N1=number(21)
N2=number(32)
N3=number(43)
N4=number(54)
N5=number(65)
print("Even numbers are: ",number.even)
print("Odd numbers are: ",number.odd)