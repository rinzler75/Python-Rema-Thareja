#way lengthy program can be done in one step also
#'{:,}'.format(value)
def comma(num,n):
    i=n
    new_str=""
    while((i+3)!=len(num)):
        new_str+=num[i:i+3]+","
        i+=3
    new_str+=num[i:len(num)]
    return new_str
str=input("Enter the number: ")
r=int((len(str))%3)
str1=""
if(r==0):
    print(comma(str,r))
else:
    for i in range(r):
        str1+=str[i]
    str1+=","
    print(str1+comma(str,r))


