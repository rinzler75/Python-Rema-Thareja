num = int(input("Enter the number has to be reversed: "))
print("The reversed number is : ",)
while(num!=0):
    temp=int(num%10)
    print(temp,end=" ")
    num=int(num/10)