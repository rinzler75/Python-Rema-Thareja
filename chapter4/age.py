date=int(input("Please enter the date of ur birth: "))
month=int(input("Please enter month of ur birth: "))
year=int(input("Please enter year of birth:"))
print("Enter today date: ")
date1=int(input())
month1=int(input())
year1=int(input())
year2 =year1-year
if(date==date1 and month==month1):
    print("00/00/",year2)
elif(month>month1):
    month2=12-month+month1
    if(date>date1):
        date2=30-date+date1
        if(date2>30):
            date2=date2-30
            month2+=1
        month2-=1
    else:
        date2=date1-date
    
    year3=year2-1
    print(date2,"days/",month2,"months/",year3,"years")
else:
    if(date>date1):
        date2=date-date1
    else:
        date2=date1-date
    month2=month1-month
    print(date2,"days/",month2,"months/",year2,"years")
