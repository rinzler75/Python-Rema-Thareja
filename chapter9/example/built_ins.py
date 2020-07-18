# these were built in's functions
class ABC():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("Var is = ",self.var)
obj=ABC(10)
obj.display()
print("Check if the object obj has attribute var ...........:", hasattr(obj,'var')) 
#this function will check if the object has the variable
getattr(obj,'var') #same as writting obj.var
setattr(obj,'var',50)
print("After setting the, var is : ",obj.var)
#if the attribute is not there it will create the new one
setattr(obj,'count',10)
print("New variable count is created and its value is : ",obj.count)
delattr(obj,"var")
#as printing a variable which doesnot exist will show an error
#print("After deleting the attribute, var is: ",obj.var)
print()
print()


#----------------------------------------
#built in's class attributes
class number():
    '''this is the doc string of the class'''
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("Var is  =",self.var1)
        print("Var is = ",self.var2)
obj=number(10,12.34)
obj.display()
#returns deictionary containing the class's or object's namespace
print("object.__dict__:",obj.__dict__)
#returns class documentation
print("object.__doc__:",obj.__doc__)
#returns name of the class
print("class.__name__:",number.__name__)
#returns name of the module in which the class is defined
print("object.__module__:",obj.__module__)
#returns the base class of in the order of their occurence
print("class.__bases__:",number.__bases__) 