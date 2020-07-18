n=int(input("Enter the number to be checked: "))
if(n!=0 and (n & (n-1))==0 ): #change in to binary and it will come true
    print("Given number is power of 2")
else: print("Its not power of 2")