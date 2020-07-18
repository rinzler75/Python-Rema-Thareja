class dictionary:
    book={}
    def __init__(self,item,brand):
        dictionary.book[item]=brand
    def display():
        for index,val in dictionary.book.items():
            print(" ",index,":",val)
item1=dictionary('shoes','adidas')
item2=dictionary('upper','nike')
dictionary.display()
