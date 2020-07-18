def decimalToBinary(n):  
  
    if(n > 1):  
        # divide with integral result  
        # (discard remainder)  
        decimalToBinary(n//2)  
  
      
    print(n%2, end=' ') 
      
      
j=int(input("Enter the number whose binary needs to be found:"))
decimalToBinary(j)  
   
