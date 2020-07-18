n=int(input("Enter the number of terms: "))
a=1
b=1
for i in range(n):
    if(i<2):
        print(1,end=" ")
    else: 
        sum=a+b
        print(sum,end=" ")
        a=b
        b=sum
