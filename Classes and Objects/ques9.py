from datetime import datetime
date=int(input("Date:"))
month=int(input("Month: "))
year=2020
bday=datetime(year,month,date,12,0,0)
nextBday=datetime(year+1,month,date,12,0,0)
if(datetime.now()>bday):
    print(nextBday-datetime.now())
else:
    print(bday-datetime.now())

#output
# Date:25
# Month: 12
# 216 days, 11:49:18.704178