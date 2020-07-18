class ABC():
    class_var=0 #CLASS VARIABLE 
    def __init__(self,var):
        ABC.class_var+=1 #ACCES METHODS
        self.var=var  #object variable
        print("The object value is :",var)
        print("The value of the class variable is: ",ABC.class_var)
    def __del__(self): #same as destructor in c++
        ABC.class_var-=1 #actions which has to be taken place when delocating an oject
        print("Object with value %d is going out of scope"%self.var)
obj1=ABC(10)
obj2=ABC(20)
obj3=ABC(30)
del obj1 #deleting the object 
del obj2
del obj3
