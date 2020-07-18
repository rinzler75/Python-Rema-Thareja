#things to remember is:
# 1. All the prime numbers are odd
# 2. and the largest prime factor of a number would be less than the square root of that number
# 3. each iteration we divide the number and find its prime factor here 
# 4. All the odd numbers which are composite will have 3,5,7 as prime factor they would be eliminated in first go

n=int(input("Enter the number whose prime factor needs to be found: "))      
while n % 2 == 0: 
    print(2,end=" ")  
    n = int(n / 2) #for finding how many of the factors are 2
          
for i in range(3,int(n**0.5)+1,2): #for finding other factors we will be traversing in odd number 
    while n % i== 0:                #whichever is composite odd numbers they are allready taken care by (2 and 3) ex: a 
        print (i,end=" " )          # number divisible by 9 is also divisble by 3 and so on
        n = int(n / i) 

if n > 2: #last number if it also prime number 
    print(n) 
    

