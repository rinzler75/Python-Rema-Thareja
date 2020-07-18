import re
string=input("Enter the string: ")
if len(string)<2:
    print(" ")
else:
    result=re.findall(r'(^\w{2}).+(\w{2}$)',string)#will give first and last two character of the string provided
    print(result) 

result=re.sub(r' \b\w',' $',string) #substitutes the first char of every first word as $ except the first wor
print(result)
