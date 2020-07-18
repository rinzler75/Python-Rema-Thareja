import re
string="Good going python"
result=re.findall(r'.',string)
print(result) #prints a list of all the char of string
result=re.findall(r'\w+',string)
print(result) #prints all the words of the string
result=re.findall(r'^\w+',string)
print(result) #prints starting word of the string
result=re.findall(r'\w+$',string)
print(result) #prints the last word of the string
result=re.findall(r'\w\w',string)
print(result) #prints a list of char in the group of two
result=re.findall(r'\b\w\w',string)
print(result) #prints a list of first two char of each word in string
result=re.findall(r'\d{2}-\d{2}-\d{4}',"Hello, my name is Shivangi and date of joining is 19-06-2021 and have experience of more than 17 years")
print(result) #prints the date in the string
result=re.findall(r'\d{2}-\d{2}-(\d{4})',"Hello, my name is Shivangi and date of joining is 19-06-2021 and have experience of more than 17 years")
print(result) #prints the joining year in string
result=re.findall(r'\b[aeiouAEIOU]\w+',"Hello, my name is Shivangi and date of joining is 19-06-2021 and have experience of more than 17 years ")
print(result) #prints all the word starting from vowels
List=['7888558965','9888855555','8905468845']
for i in List:
    result=re.findall(r'[7-9]{1}[0-9]{9}',i)
    if result:
        print(result,end=" ")
# prints all the numbers starting from 7,8,9


