class Mean():
    def __init__(self,num):
        self.num=num
        
    def mean(a,b):
        mean=(a.num+b.num)/2
        print("The mean is : ",mean)
obj1=Mean(10)
obj2=Mean(20)
Mean.mean(obj1,obj2)