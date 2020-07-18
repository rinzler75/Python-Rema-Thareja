#multiple inheritances 
class Bill:
    
    def __init__(self,items,price):
        self.total=0
        self.items=items
        self.price=price
        for i in self.price:
            self.total+=i
    
    def display(self):
        print("\n ITEM \t\t\t PRICE")
        for i in range(len(self.items)):
            print(self.items[i],"\t\t",self.price[i])
        print("*************************")
        print("TOTAL= ",self.total)


class Cash_payment(Bill):
    
    def __init__(self,items,price,deno,value):
        Bill.__init__(self,items,price)
        self.deno=deno
        self.value=value
    
    def show_Cash_Payment_Details(self):
        Bill.display(self)
       
        for i in range(len(deno)):
            print(deno[i],"*",value[i],"=",deno[i]*value[i])


class Cheque_Payment(Bill):
    def __init__(self,items,price,cno,name):
        Bill.__init__(self,items,price)
        self.cno=cno
        self.name=name
    def show_Check_Payment_Details(self):
        Bill.display(self)
        print("CHEQUE NUMBER: ",self.cno)
        print("BANK NAME : ",self.name)


items=["External Hard Disk","Ram","Printer","Pen Drive"]
price=[5000,2000,6000,800]
option=int(input("Would you like to pay by cheque or cash(1/2): "))
if option==1:
    name=input("Enter the name of the bank: ")
    cno=input("Enter the cheque number : ")
    Cheque=Cheque_Payment(items,price,cno,name)
    Cheque.show_Check_Payment_Details()
else:
    deno=[10,20,50,100,500,2000]
    value=[1,1,1,20,4,5]
    CP= Cash_payment(items,price,deno,value)
    CP.show_Cash_Payment_Details()
