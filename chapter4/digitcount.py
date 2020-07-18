n=int(input("Enter the number: "))
i=0
while(n!=0):
    if((int(n%10))!=0):
        i=i+1
    n=n/10
print("Digits are:",i)