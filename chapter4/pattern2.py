#classy and logical one

n=5
for i in range(1,n+1):
    
    for k in range(n,i,-1): #for spaces
        print(" ",end="")
   
    for j in range(1,i+1):
        print(end=""+str(j)) #for numbers
    
    print()