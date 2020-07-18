class train:
    
    no_of_seats_st={}
    no_of_seats_2_tier={}
    no_of_seats_3_tier={}
    i=0
    for i in range(3):
        no_of_seats_st[i+1]="UNBOOKED"
    for i in range(3):
        no_of_seats_2_tier[i+1]="UNBOOKED"
    for i in range(3):
        no_of_seats_3_tier[i+1]="UNBOOKED"
    def set(self):
        key=0
        val=""
        print("1. Standard Ticket")
        print("2. 2nd Tier")
        print("3. 3rd Tier")
        j=int(input("Enter ur choice: "))
        if j==1:
            self.name=input("Enter the name for reservation: ")
            
            for key,val in train.no_of_seats_st.items():
                if val=="UNBOOKED":
                    train.no_of_seats_st[key]=self.name
                    self.key=key
                    self.cat="Standard Ticket"
                    break
                elif key==3 and val!="UNBOOKED":
                    print("Seats full")
                    SystemExit(0)
        elif j==2:
            
            self.name=input("Enter the name for reservation: ")
            
            for key,val in train.no_of_seats_2_tier.items():
                if val=="UNBOOKED":
                    train.no_of_seats_2_tier[key]=self.name
                    self.key=key
                    self.cat="2nd Tier"
                    break
                elif key==3 and val!="UNBOOKED":
                    print("Seats full in second tier")
                    SystemExit(0)
        
        elif j==3:
            self.name=input("Enter the name for reservation: ")
            
            for key,val in train.no_of_seats_3_tier.items():
                if val=="UNBOOKED":
                    train.no_of_seats_3_tier[key]=self.name
                    self.key=key
                    self.cat="3rd Tier"
                    break
                elif key==3 and val!="UNBOOKED":
                    print("Seats full in Third Tier tier")
                    SystemExit(0)

    def display():
        print("For standard Tier : ",train.no_of_seats_st)
        print("For 2nd Tier : ",train.no_of_seats_2_tier)
        print("For 3rd Tier : ",train.no_of_seats_3_tier)

class reservation(train):
    count_st=0
    count_2_tier=0
    count_3_tier=0
    def seats_booked():
        
        for key,val in train.no_of_seats_st.items():
            if val!="UNBOOKED":
                reservation.count_st+=1
        print("Standard Tier Booked Tickets: ",reservation.count_st)
        
        for key,val in train.no_of_seats_2_tier.items():
            if val!="UNBOOKED":
                reservation.count_2_tier+=1
        print("Second Tier Booked Tickets: ",reservation.count_2_tier)
        
        for key,val in train.no_of_seats_3_tier.items():
            if val!="UNBOOKED":
                reservation.count_3_tier+=1
        print("Second Tier Booked Tickets: ",reservation.count_3_tier)
    def book(self):
        self.set()
        print("-------------------TICKET-------------------------")
        print("Name: ",self.name)
        print("Seat Alloted: ",self.key)
        print("Category: ",self.cat)
    def cancel(self):
        key=0
        val=""
        print("1. Standard Ticket")
        print("2. 2nd Tier")
        print("3. 3rd Tier")
        j=int(input("Enter ur choice: "))
        if j==1:
            self.cancel_key=int(input("Enter the seat of reseservation: "))
            
            for key,val in train.no_of_seats_st.items():
                if key==self.cancel_key:
                    train.no_of_seats_st[key]="UNBOOKED"
                    
            reservation.count_st-=1
            print("TICKET CANCELLED SUCCESSFULLY")
        elif j==2:
            
            self.cancel_key=int(input("Enter the seat of reseservation: "))
            
            for key,val in train.no_of_seats_2_tier.items():
                if key==self.cancel_key:
                    train.no_of_seats_st[key]="UNBOOKED"
                    
            reservation.count_2_tier-=1
            print("TICKET CANCELLED SUCCESSFULLY")
        
        elif j==3:
            self.cancel_key=int(input("Enter the seat of reseservation: "))
            
            for key,val in train.no_of_seats_3_tier.items():
                if key==self.cancel_key:
                    train.no_of_seats_st[key]="UNBOOKED"
                    
            reservation.count_3_tier-=1
            print("TICKET CANCELLED SUCCESSFULLY")

passenger1=reservation()
passenger1.book()
reservation.seats_booked()
train.display()
passenger1.cancel()
train.display()

        
