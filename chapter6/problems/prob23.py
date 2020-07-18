str='''hello i am navnit.
       how are you?'''
str=str+"\n     aur suar kaisa hai"
new_str=str.splitlines()
str1=''
for i in new_str:
    str1=str1+i.strip()+"\n"
print(str1)