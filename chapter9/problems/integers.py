#prob 13
class integer_op():
    num_list=[]
    
    def read(self):
        for i in range(10):
            n=int(input("Enter number %d :"%(i+1)))
            integer_op.num_list.append(n)
            
    def largest(self):
        max=0
        for i in integer_op.num_list:
            if i>max:
                max=i
        return max
    def smallest(self):
        min=99999
        for i in integer_op.num_list:
            if i<min:
                min=i
        return min
    
    def sum(self):
        total=0
        for i in integer_op.num_list:
            total+=i
        return total

    def display(self):
        ch=0
        while(ch!=7):
            print("\n\n*******MENU******")
            print('''1.READ
                     2.DISPLAY
                     3.LARGEST
                     4.SMALLEST
                     5.SUM
                     6.MEAN
                     7.EXIT''')
            ch=int(input("Enter your choice: "))
            if ch==1:
                print("Enter the numbers:- ")
                integer_op.read(self)
            elif ch==2:
                print("The list is : ",integer_op.num_list)
            elif ch==3:
                print("The largest element is : ",integer_op.largest(self))
            elif ch==4:
                print("The smallest element is : ",integer_op.smallest(self))
            elif ch==5:
                print("The sum of elements is : ",integer_op.sum(self))
            elif ch==6:
                print("The mean of the elements is :",integer_op.sum(self)/7)
    

            
s=integer_op()
s.display()

                


