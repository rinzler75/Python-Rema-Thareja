a=[1,2,3,4,5,6,7,8]
b=len(a)
max=0
for i in range(int(b/2),b):
    if a[i]>max:
        max=a[i]
print(max)

#-----------prob33
l=[x for x in range(1,21)]
new_l=[]
for i in l:
        if i%3==0:
                l.remove(i)
print(l)