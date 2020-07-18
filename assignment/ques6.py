def chop(x):
    new_list=[]
    for i in range(0,len(x)):
        if(i!=0 or i!=(len(x)-1)):
            new_list.append(x[i])
    return

def middle(x):
    new_list1=[]
    for i in range(0,len(x)):
        if(i==0 or i==(len(x)-1)):
            continue
        else:
            new_list1.append(x[i])
    return new_list1

lst=[1,2,3,4,5,6,7,8,9]
lst=middle(lst)
print("New list is : ",lst)
print("Calling chop",chop(lst))