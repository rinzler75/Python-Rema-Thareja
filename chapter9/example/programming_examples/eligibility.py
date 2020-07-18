import datetime
class Person():
    def __init__(self,name,dob):
        self.name=name
        self.dob=dob
    def check(self):
        today=datetime.date.today()
        age=today.year-self.dob.year
        if today< datetime.date(today.year,self.dob.month,self.dob.day):
            age-=1
        if age>=18:
            print(self.name,"Congratulations ..... you are eligible to vote.")
        else:
            print(self.name,"Sorry...........you should be atleast 18 years old to caste a vote.")
P=Person("Saesha",datetime.date(1998,12,25))
P.check()