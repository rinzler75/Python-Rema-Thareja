#took me morning to evening

with open("A:\\python\\chapter7\\problems\\file2.txt","w") as file:
    file.write("")
import re
a='''Come on
Hello. i am Shivangi My
cadet number is 4175
my naem is navnit'''
str=a.split("\n")
file=open("A:\\python\\chapter7\\problems\\file2.txt","a")
for i in range(len(str)):
    if '.' not in str[i]:
        file.write(str[i]+"\n")
    else:
        sea1=re.search(r'(\w+[.])',str[i])
        sea=sea1.group(1)
        line=str[i].split(" ")
        for j in range(len(line)):
            if(sea==line[j]):
                break
            else:
                file.write(line[j]+" ")
        file.write(sea+" ")
        if j<len(line):
            for k in range(j+1,len(line)):
                if line[k].isalpha():
                    str1=line[k].upper()
                    file.write(str1+" ")
                elif line[k].isdigit():
                    file.write("("+line[k]+") ")
        file.write("\n")
        if(i<len(str)):
            for l in range(i+1,len(str)):
                line=str[l].split(" ")
                for m in range(len(line)):
                    if line[m].isalpha():
                        str1=line[m].upper()
                        file.write(str1+" ")
                    elif line[m].isdigit():
                        file.write("("+line[m]+") ")
                file.write("\n") 
        break
file.close()


    