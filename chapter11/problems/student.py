class student:
    def __init__(self,roll_no,m1,m2,m3):
        self.roll=roll_no
        self.marks=[]
        self.marks.append(m1)
        self.marks.append(m2)
        self.marks.append(m3)
class student2(student):
    def stores(self):
        sum=0
        for i in self.marks:
            sum+=i
        self.avg=sum
    
a=student2(63,98,92,96)
a.stores()
print(a.avg)