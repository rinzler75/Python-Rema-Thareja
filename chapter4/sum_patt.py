import math
x=int(input("Enter the value of x: "))
sum=0
n=int(input("Please enter the precision: "))
for i in range(n):
    sum+=((-1)**(i+1))*(x**(i+1))
print(sum)
sum=0
y = int(input("Please enter the number of terms: "))
for j in range(1,y+1):
    for k in range(1,j+1):
        sum=sum+k
print(sum)
sum=0
z=int(input("Please enter the value of z: "))
a=int(input("Please enter the precision(at least more than three): "))
for m in range(a):
    sum=sum+(((-1)**m)*(z**m))/math.factorial(m)
print(sum)