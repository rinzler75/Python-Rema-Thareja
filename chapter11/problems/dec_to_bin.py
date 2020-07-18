q=25
b=[]
while q!=(1 or 0):
    r=q%2
    q=int(q/2)
    b.insert(0,r)
b.insert(0,q)
print(b)
str1=''
for i in b:
    str1+=str(i)
dec=int(str1)
print(dec)