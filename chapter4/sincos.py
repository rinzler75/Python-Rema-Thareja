import math
PI=3.141
for i in range(0,361,15):
    print("    ",i,end="  ")
print("sin ",end="")
for i in range(0,361,15):
    print(math.sin((PI/180)*i),end=" ")
print()
print("cos ",end="")
for i in range(0,361,15):
    print(math.cos((PI/180)*i),end=" ")