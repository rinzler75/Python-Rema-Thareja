class Book:
    def __init__(self):
        self.title=""
        self.author=""
        self.price=0
    def read(self):
        self.title=input("Enter Book Title :")
        self.author=input("Enter Book author: ")
        self.price=float(input("Enter book price: "))
    def display(self):
        print()
        print()
        print("Title : ",self.title)
        print("Author : ",self.author)
        print("Price : ",self.price)
my_books=[]
ch='y'
while (ch=='y'):
    print('''
    1. Add New Book
    2. Display Books
    ''')
    choice = int(input("Enter your choice: "))
    if (choice==1):
        book=Book()
        book.read()
        my_books.append(book)
    elif(choice==2):
        for i in my_books:
            i.display()
    else:
        print("Invalid choice")
    ch=input("Do you want to continue...(y/n)")
print("Bye")   