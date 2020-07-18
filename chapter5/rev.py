# is also true for reversing the strings
def rev(str,length):
    global str1
    if(length==0):
        return str1
    str1=str1+str[length-1]
    length-=1
    return rev(str,length)
str1=''
num=input("Enter the number: ")
l=len(num)
print("Reverse number: "+rev(num,l))
