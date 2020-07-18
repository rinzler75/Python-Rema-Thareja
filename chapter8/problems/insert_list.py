ele=input("The element which needs to be inserted: ")
a=[]
a.append(ele)
pos=int(input("The position for which it needs to be inserted: "))
l=[1,2,3,4,6,7]
new_list=l[0:pos]+a+l[pos:len(l)]
print(new_list)
del a

#using a while loop
new_list=[]
i=0
j=0
while i<len(l)+1:
    if i==pos:
        new_list.append(ele)
    else:
        new_list.append(l[j])
        j+=1
    i+=1
print(new_list)