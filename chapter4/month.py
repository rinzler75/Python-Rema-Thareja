#good code
start_day=int(input("Enter the starting day of the month: ")) #asking about the day
num_of_days=int(input("Enter the number of days in that month: ")) #total no of days in that month
print("Sun  Mon  Tue   Wed  Thu  Fri  Sat")
print("-------------------------------------")

for i in range(start_day-1):
    print(end="      ")

i=start_day-1

for j in range(1,num_of_days+1):
    if(i>6): #over here this statement will get executed at i=6 also
        print()
        i=0

    else:
        i=i+1
        print(j,end="    ")
