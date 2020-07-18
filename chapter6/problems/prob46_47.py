import re
str=input("Enter the name: ")
pattern=re.search(r'(\w).* (\w).* (\w)',str)
print(pattern.group(1)+pattern.group(2)+pattern.group(3))
pattern1=re.search(r'(\w).* (\w).* (\w+)',str)
print(pattern1.group(1)+"."+pattern1.group(2)+"."+pattern1.group(3))