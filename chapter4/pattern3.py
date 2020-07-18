n=5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(end=""+str(k))
    for l in range(k,1,-1): #or u can relate it to the topmost condition for l in range(i-1,0,-1),print(l,end="")
        print(end=""+str(l-1))
    print()

    