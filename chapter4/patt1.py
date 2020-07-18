for i in range(3):
    if(i==0):
        print("$ * * * *")
    elif(i==2):
        print("* * * * $")
    else:
        for j in range(1,6,2):
            print("*",end="")
            for k in range(j): #for spacing of the program
                print(end=" ")
            print(end="$")
            for l in range(6-j):
                print(end=" ")
            print(end="*")
            print()


#better code is here
print("Type the number of rows: ")
n=int(input())
for p in range(1,n+1):
        for q in range(1,n+1):
                if(p==1 or p==n):
                    if(p==q):
                        print("$ ",end="")
                    else:
                        print("* ",end="")
                elif(q==1 or q==n):
                        print("* ",end="")
                elif(p==q):
                        print(end="$ ")
                else:
                        print(end="  ")
        print()            
        