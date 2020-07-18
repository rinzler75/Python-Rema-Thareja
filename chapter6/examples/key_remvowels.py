#example to show caesar cipher
#if key value is 3 every word in the message should be added with key
message="HelloWorld"
key=3
for i in message:
    print(chr(ord(i)+key),end=" ")

#another example which removes vowels from a string and return
string=input("Enter the string: ")
newstr=''
for i in string:
    if i in "aeiouAEIOU":
        continue
    else:
        newstr+=i
print(newstr)
