import calendar
y=int(input("Enter the Year: "))
m=1
print("\n*******CALENDAR******")
Cal=calendar.TextCalendar(calendar.SUNDAY)
#an instance of TextCalendar class is created and calendar.Sundat means that you want to start displayinng the
#  calendar from sunday
i=1
while(i<=12):
    print()
    print(Cal.prmonth(y,i))
    i+=1
#prmonth() is a function of the class that prints the calendar for given month and  year