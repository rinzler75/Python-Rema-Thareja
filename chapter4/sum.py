#calculates the average of first n numbers
n=int(input("Enter the value of n: "))
avg=0.0
s=0
for i in range(1,n+1): #here 1 is included but n+1 is not included
    s=s+i
avg=s/n
print(" The sum of first",n,"natural numbers is",s)
print("The average is :",avg)