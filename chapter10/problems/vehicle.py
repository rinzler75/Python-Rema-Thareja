class vehicle:
    def detail(self):
        raise NotImplementedError
    def display(self):
        raise NotImplementedError

class car(vehicle):
    def detail(self):
        self.seats=int(input("Enter the no of seats of car: "))
        self.tyres=int(input("Enter the number of tyres in the car: "))
        self.company=input("Enter the brand of the car: ")
    
    def display(self):
        print("\n\n*******CAR******")
        print("Seats in the car: ",self.seats)
        print("Tyres in the car: ",self.tyres)
        print("Brand of the car: ",self.company)

class Motorcycle(vehicle):
    def detail(self):
        self.seats=int(input("Enter the no of seats of Motorcycle: "))
        self.tyres=int(input("Enter the number of tyres in the Motorcycles: "))
        self.company=input("Enter the brand of the Motorcycle: ")
    
    def display(self):
        print("\n\n ******MOTORCYCLE******")
        print("Seats in the Motorcycle: ",self.seats)
        print("Tyres in the Motorcycle: ",self.tyres)
        print("Brand of the Motorcycle: ",self.company)
        
class truck(vehicle):
    def detail(self):
        self.seats=int(input("Enter the no of seats of truck: "))
        self.tyres=input("Enter the number of tyres in the truck: ")
        self.company=input("Enter the brand of the truck: ")
    
    def display(self):
        print("\n\n******TRUCKS*****")
        print("Seats in the Truck: ",self.seats)
        print("Tyres in the Truck: ",self.tyres)
        print("Brand of the Truck: ",self.company)

C=car()
C.detail()
m=Motorcycle()
m.detail()
t=truck()
t.detail()
C.display()
m.display()
t.display()

        