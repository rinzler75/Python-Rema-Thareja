class fraction:
    def get_data(self):
        self.__num=int(input("Enter the numerator: "))
        self.__denom=int(input("Enter the denomenator: "))
        if(self.__denom==0):
            print("Fraction not possible")
            exit()
    def display_data(self):
        self.__simplify()
        print(self.__num,"/",self.__denom)

    def __simplify(self):
        print("The simplified fraction is: ")
        common_divisor=self.__GCD(self.__num,self.__denom)
        self.__num=self.__num/common_divisor
        self.__denom=self.__denom/common_divisor
    def __GCD(self,a,b):
        if b==0:
            return a
        else:
            return self.__GCD(b,a%b)
f=fraction()
f.get_data()
f.display_data()