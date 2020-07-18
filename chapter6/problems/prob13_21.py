import re
str=input("Enter the string: ")
pattern=re.findall(r'\w+',str)
n=len(pattern)
for i in range(n): #bubb;e sort
    for j in range(n-i-1):
        if pattern[j] > pattern[j+1] :
                pattern[j], pattern[j+1] = pattern[j+1], pattern[j]
print(pattern)


str='''hello i am navnit.
how are you?'''
str=str+"\naur suar kaisa hai"
new_str=str.splitlines()
str1=''
for i in new_str:
    str1=str1+i.strip()+" "
print(str1)