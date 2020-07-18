import re

str=input("Enter the main string: ")
str1=input("Enter the string to be inserted: ")
pos=int(input("Enter the position it has to be inserted: "))
new_str=str[0:pos+1]+" "+str1+" "+str[pos+1:len(str)]
print(new_str)

str1=input("Enter the string has to be deleted: ")
new_str=re.sub(str1,"",str)
print(new_str)
print(str)
str1=input("Enter the string which has to be replaced: ")
str2=input("Has to be replaced with: ")
num=str.find(str1,0,len(str))
str3=str[0:num]
str4=str[num+len(str1):len(str)]
print(str3+str2+str4)
