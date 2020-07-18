b_day={}
while True:
    name=input("Enter the name: ")
    if name in b_day.keys():
        print("The birth date is: ",b_day[name])
    elif name=='-1':break
    else:
        new_key=name
        new_bday=input("Enter the birth date(dd/month):")
        b_day[new_key]=new_bday
sort=sorted(b_day)
sort_bday={}
for i in sort:
    sort_bday[i]=b_day[i]
print(sort_bday)