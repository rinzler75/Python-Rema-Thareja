class Square:
    def __init__(self,side):
        self.__side=side
    @property
    def area(self):
        return self.__side*self.__side
S=Square(9)
print(S.area)#remove property and see u will find the difference