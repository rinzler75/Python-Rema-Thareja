n=int(input("Enter the number for which factorial needs to be found: "))
fact=1
if(n==0 or n==1) :
    print("Factorial is : 1")
else:
    for i in range(2,n+1):#2 is included till n
        fact=fact*i
    print("Factorial is : ",fact)