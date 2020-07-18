class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        

    def area(self):
        return self.length * self.breadth 
    @classmethod
    def square(cls,side):
        return cls(side,side)
    # as u can see u want to initialize the square function only with different variable
    #so we have provided another function which will take different parameters and 
    #provide to initialise function and simuntaneously the object would be created
    #and then whatever function u need can be calculated
S=Rectangle.square(10)
print("AREA = ",S.area())