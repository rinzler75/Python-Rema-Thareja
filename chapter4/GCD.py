#finds the gcd non -recursive way
num1=int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if(num1>num2):
    dividend=num1 #numerator
    divisor=num2  #denomenator
else:
    dividend=num2
    divisor=num1
while (divisor!=0):
    remainder=int(dividend%divisor) #num/denom ka remainder
    dividend=divisor
    divisor=remainder
print("GCD Of (",num1,",",num2,") is ",dividend)