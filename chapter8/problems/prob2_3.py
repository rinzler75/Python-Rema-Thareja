#making a list of 5 random number
import random
import string
b=[]
for i in range(5):
    a=random.randint(1,100)
    b.append(a)
print(b)
b.clear()
print(b)
j=0
b=[string.ascii_lowercase[i] for i in range(10)]
print(b[0:3])
r=random.randint(0,7)
print(b[r:r+3])
print(b[r:10])

def str_a(x):
    return ord(x)
j=list(map(str_a,b))
print(j)
