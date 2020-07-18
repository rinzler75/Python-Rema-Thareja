def conct(str1,str2):
    global str,i
    str=str+str2
    i+=1
    l=len(str)
    l1=len(str1)
    l2=len(str2)
    if(l==(l1+l2)):
        return str
    return conct(str1,str2)
i=0
str=''
s1=input("First string: ")
str=s1
s2=input("Second string: ")
s=conct(s1,s2)
print(s)