import re
str=input("Enter the string: ")
ch=input("Enter the character: ")
string=str
while(string.find(ch,0,len(string))!=-1): #deleting all the occurence of ch from a string
    a=string.find(ch,0,len(string))
    string=string[0:a]+string[a+1:len(string)]
print(string)

#deleting the occurece of a given word from the string
str1=input("Enter the word to be deleted: ")
pattern=re.findall(r'\w+',str)

new_str=''
for i in pattern:
    if i==str1:
        continue
    else:
        new_str+=" "+i
print(new_str.strip())