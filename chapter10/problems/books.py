class publish:
    def __init__(self):
        self.title=input("Enter the title: ")
        self.price=int(input("Enter the price : "))

class book(publish):
    def __init__(self):
        super().__init__()
        self.no_of_pages=int(input("Enter the number of pages: "))
    def display(self):
        print(self.title,"of ",self.no_of_pages,"Pages and Price Rs.",self.price)

class audio_visual(publish):
    def __init__(self):
        super().__init__()
        self.play_time=int(input("Enter the playtime in hours: "))
    def display(self):
        print(self.title,"of Play time",self.play_time,"Hours and Price Rs.",self.price)

b1=book()
b1.display()
a1=audio_visual()
a1.display()
