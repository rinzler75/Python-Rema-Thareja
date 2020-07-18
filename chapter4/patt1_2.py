print("Type the number of rows: ")
n=int(input())
for i in range(1,n+1):#for the rows 
        for j in range(1,n+1):#for the coloumns
                if(i==1 or i==n):
                        if(i==j or i==(n-j)+1):
                                print("$ ",end="")
                        else:
                                print("* ",end="")
                elif(j==1 or j==n):
                        print("* ",end="")
                elif(i==j or i==(n-j+1)):
                        print(end="$ ")
                else:
                        print(end="  ")
        print()            
        