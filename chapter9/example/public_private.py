class ABC():
    def __init__(self, var1,var2):
        self.var1=var1
        self.__var2=var2 #any variable defined with double underscore is defined as private 
    def display(self):
        print("From class method, Var1 = ",self.var1)
        print("From class method, Var2= ",self.__var2) #it will be accessed inside this class
obj=ABC(10,20)
obj.display()
print("From main module, var1 =",obj.var1)

#case1
#print("From main module, var2 =",obj.__var2) #this line will raise AttributeError(while outside the class)
#while if u want to access the private variable inside the class

#case2
print("From main module, Var2 = ",obj._ABC__var2) #only one underscore at starting

#______________________________________________________private method
class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("From the class method,Var= ",self.__var)
obj=abc(10)
obj._abc__display()
print()
print()

#------------------------------------------
#calling a class method from another class
def scale_10(x):
    return x*10
class number():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is =",self.var)
    def add_2(self):
        self.var+=2
        self.display() #calling another function of the class from another method
    def modify(self):
        self.var=scale_10(self.var)
        self.display() #calling a method which is in global namespace
obj=number(10)
obj.add_2()
obj.modify()
#modifying the values of object during run time, similar like java
obj.var=20
obj.display()
#u can even delete the objects created


