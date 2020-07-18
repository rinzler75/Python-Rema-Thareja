num=int(input("Enter the number to be checked: "))
ic=0
for i in range(2,num):
    if(num%i==0):
        ic=1
        print("The given number is a COMPOSITE NUMBER")
        break
if(ic==0):
    print("The given number is a PRIME NUMBER")

