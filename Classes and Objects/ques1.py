class point:
    x,y=0,0
class Rectangle:
    width,height,corner_x,corner_y=0,0,0,0
    def center(self):
        p=point()
        p.x=self.corner_x+self.width/2
        p.y=self.corner_y+self.height/2
        return p
    def perimeter(self):
        return 2*(self.width+self.height)
    def area(self):
        return self.width*self.height

box=Rectangle()
box.corner_x=int(input("Enter the right down corner x cordinate: "))
box.corner_y=int(input("Enter the right down corner y cordinate: "))
box.width=int(input("Enter the width of rectangel: "))
box.height=int(input("Enter the width of rectangle:  "))
c=point()
c=box.center()
print("The Center of the rectangle is : ",c.x,",",c.y)
print("Perimeter of the rectangle is: ",box.perimeter())
print("Area of the rectangle  is: ",box.area())

##Output
# Enter the right down corner x cordinate: 10
# Enter the right down corner y cordinate: 20
# Enter the width of rectangel: 10
# Enter the width of rectangle:  20
# The Center of the rectangle is :  15.0 , 30.0
# Perimeter of the rectangle is:  60
# Area of the rectangle  is:  200