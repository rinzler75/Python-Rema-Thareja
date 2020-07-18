class Polygon:
    def get_data(self):
        raise NotImplementedError
    def area(self):
        raise NotImplementedError

class Rectangle(Polygon):
    def get_data(self):
        self.length=float(input("Enter the length of the Rectangle : "))
        self.breadth=float(input("Enter the breadth of the Rectangle: "))
    def area(self):
        return self.length*self.breadth
class Triangle(Polygon):
    def get_data(self):
        self.base=float(input("Enter the base of the triangle: "))
        self.height=float(input("Enter the Height of the triangle: "))
    def area(self):
        return 0.5*self.base*self.height
R=Rectangle()
R.get_data()
print("Area of the Rectangle: ",R.area())
T=Triangle()
T.get_data()
print("Area of the triangle : ",T.area())