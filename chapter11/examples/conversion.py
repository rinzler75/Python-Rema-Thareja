class Distance_m:
    def __init__(self,m):
        self.m=m
    def display(self):
        print("Distance in meteres: ",self.m)
    def mts(D):
        return D.km*1000
class Distance_km:
    def __init__(self,km):
        self.km=km
    def display(self):
        print("Distance in kilometers is : ",self.km)
    def km(D):
        return D.m/1000
Dm=Distance_m(12345)
Dm.display()
print("Distance in kms: ",Distance_km.km(Dm))
DKm=Distance_km(12.345)
DKm.display()
print("Distance in metres: ",Distance_m.mts(DKm)) 