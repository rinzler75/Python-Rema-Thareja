def reverse(str): #using string concatenation
    new_str=''
    i=len(str)-1
    while i>=0:
        new_str+=str[i]
        i-=1
    return new_str
s=input("Enter the string to be reversed: ")
print("The reversed string is : "+reverse(s))