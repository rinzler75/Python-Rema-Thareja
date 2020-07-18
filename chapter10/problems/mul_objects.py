class Country:
    def __init__(self,name):
        self.name=name
    def capital(self):
        raise NotImplementedError

class India(Country):
    def capital(self):
        return 'New Delhi'

class USA(Country):
    def capital(self):
        return 'Washington'

countries=[India('India'),USA('USA')]
for country in countries:
    print(country.name+':'+country.capital())
    