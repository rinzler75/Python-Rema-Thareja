class ABC():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var) #returns a string representation of object variables
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var-obj.var
obj=ABC("abcdef",10)
print("The value stored in object is: "+repr(obj)) #as returned object is string
print("The length of the name stored in object is: ",len(obj))
obj1=ABC("ghijkl",1)
val=obj.__cmp__(obj1)
if val==0:
    print("Both values are equal")
elif val<0:
    print("First value is lesser than second value")
else:
    print("Second value is less than first value")

#----------------------------------------
class Numbers:
    def __init__(self, myList):
        self.myList=myList
    def __getitem__(self,index):
        return self.myList[index] 
    #gets the item according to the fortold index
    def __setitem__(self,index,val):
        self.myList[index]=val
    
NumList=Numbers([1,2,3,4,5,6,7,8,9])
print(NumList[5])
NumList[3]=10 #thats how the work is defined in class
print(NumList.myList)
