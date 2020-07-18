class sample:
    def __init__(self,val):
        self.val=val
    def get_val(self):
        return self.__val
    def set_val(self,val):
        self.__val=val
    val=property(get_val,set_val)
S=sample(20)
S.val=100
print(S.val)

#---------------to provide better setter and getter u can make ur methods private
class sample_1:
    def __init__(self,val1):
        self.__val1=val1
    def __get_val1(self):
        return self.__val1
    def __set_val1(self,val1):
        self.__val1=val1
    val=property(__get_val1,__set_val1)
S=sample_1(20)
S.val1=100 #if u dont do this ur piece of code wont execute u made the class private as u 
#cant modify the values 
print(S.val1)