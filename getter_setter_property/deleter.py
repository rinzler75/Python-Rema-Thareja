class Sample_2:
    def __init__(self,val2):
        self.val2=val2
    @property
    def val(self):
        return self.val2
    @val.setter
    def val(self,val2):
        self.__val2=val2
    @val.deleter
    def val(self):
        print("Deleting object attribute")
        del self.val2
S=Sample_2(20)
S.val=100
print(S.val)
del S.val