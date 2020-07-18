from datetime import timedelta
class Time:
    def __init__(self,x,y,z):
        self.time=timedelta(hours=x,minutes=y,seconds=z)
    def subtract(self,a):
        diff = Time(0,0,0)
        diff.time=self.time-a.time
        return str(diff.time)
time1=Time(10,50,15)
time2=Time(9,50,12)
print("The Diff between two events is: ",time1.subtract(time2))

#output
# The Diff between two events is:  1:00:03