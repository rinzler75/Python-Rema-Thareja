#removing a particular indexed char from the string
str=input("Enter the string: ")
i=int(input("Enter the index value of the char which has to be removed: "))
str1=str[0:i]
str2=str[i+1:len(str)]
new_str=str1+str2
print(new_str)
new_str=' '
for j in range(len(str)):
    if j%2==0:
        new_str+=str[j]
    else:
        continue
print(new_str)