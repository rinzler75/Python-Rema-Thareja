#program to call the init method of all the classes in multiple inheritances
class Base1(object):
    def __init__(self):
        print("Base1 Class")
        super(Base1,self).__init__()
class Base2(object):
    def __init__(self):
        print("Base2 Class")
class Derived(Base1,Base2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived Class")
D=Derived()