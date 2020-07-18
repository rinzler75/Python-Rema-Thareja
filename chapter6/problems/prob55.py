import random
str=input("Enter the string to be encrypted: ")
key=random.randint(1,1000)
for i in str:
    print(chr(ord(i)*key),end=" ")