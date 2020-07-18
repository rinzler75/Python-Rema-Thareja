import re
str=input("Enter the string: ")
pattern=re.finditer(r"not",str)
pattern1=re.finditer(r"poor",str)
for i in pattern:
    print(i.span())
for j in pattern1:
    print(j.span())

if (re.search(r"not.*poor",str)):
    if(re.search("poor bad",str)):
        new_str=re.sub(r"not.*poor","good",str)
        print(new_str)
