for i in range(5):
    for j in range(i+1):
        print(end="* ")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print(end="* ")
    print()

for i in range(1,5):
    j=i
    if(i==1):
        print(1)
        continue
    while(j!=0):
        print(j,end="")
        j=j-1
    j=2
    print(j,end="")
    while(j!=i):
        j+=1
        print(j,end="")
    print()
    
for i in range(5,0,-1):
    for j in range(6-i):
        print(end=" ")
    for k in range(6-i,6):
        print(k,end=" ")
    print()

for i in range(1,6):
    for j in range(i):
        print(j+1,end="")
    print()
        
