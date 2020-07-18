class student:
    def __init__(self,first_name,second_name):
        self.__first_name=first_name
        self.__second_name=second_name
    @property
    def name(self):
        return "%s %s"%(self.__first_name,self.__second_name)
S=student("Shivangi","Arul")
S.__first_name='kumar'#here this function wont matter as the object attributs are private
#they cant be changed
print(S.name)
