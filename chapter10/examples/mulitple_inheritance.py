class Base1(object):
    def __init__(self):
        print("Base1 Class")
        #super(Base1,self).__init__() #uncomment this statement for the regularized execution
class Base2(object):
    def __init__(self):
        print("Base2 Class")
class Derived(Base1,Base2):
    pass
d= Derived()