num=int(input("Enter the number:"))
power=int(input("Enter the power: "))
result=1
for i in range(power):
    result*=num
print("The result is: ",result)