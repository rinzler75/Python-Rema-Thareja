class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def midpoint(self,a,b):
        mid=Point(0,0)
        mid.x=(a.x+b.x)/2
        mid.y=(a.y+b.y)/2
        return mid
    def __str__(self):
        return ("(%d,%d)"%(self.x,self.y))
    def reflex_x(self):
        ref=Point(0,0)
        ref.x=self.x
        ref.y=-(self.y)
        return ref
p=Point(10,20)
q=Point(20,40)
print("The midpoint is : ",p.midpoint(p,q))
print("The reflex of point ",p,"is",p.reflex_x())
print("The reflex of point ",q,"is ",q.reflex_x())

##output
# The midpoint is :  (15,30)
# The reflex of point  (10,20) is (10,-20)
# The reflex of point  (20,40) is  (20,-40)