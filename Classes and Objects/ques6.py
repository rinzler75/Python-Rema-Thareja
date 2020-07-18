from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")
day=today.strftime("%A")
print("Today Date :", d1,"\nWeekDay: ",day)

# output
# Today Date : 22/05/2020
# WeekDay:  Friday
