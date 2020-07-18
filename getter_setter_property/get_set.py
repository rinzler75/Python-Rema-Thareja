class sample:
    def __init__(self,val):
        self.__val=val
    def get_val(self):
        return self.__val
    def set_val(self,val):
        self.__val=val
s=sample(20)
s.set_val(10)
print(s.get_val())