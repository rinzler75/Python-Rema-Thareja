class Fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def colour(self):
        raise NotImplementedError() #if not implemented NotImplementedError is raised
class Mango(Fruit):
    def taste(self):
        return "Sweet"
    def rich_in(self):
        return "Vitamin A"
    def colour(self):
        return "Yellow"
Alphanso=Mango()
print(Alphanso.taste(),Alphanso.rich_in(),Alphanso.colour())