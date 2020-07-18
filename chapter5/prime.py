ic=1
def is_prime(num):
    for i in range(2,num):
        if(num%i==0):
            return 0

num1=int(input("Enter the number to be checked: "))    
ic=is_prime(num1)        
if(ic==0):
    print("COMPOSITE NUMBER")
else:
    print("PRIME NUMBER")

