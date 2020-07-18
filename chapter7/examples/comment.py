#program copies one python script into another in such a way that all the 
#comment lines are skipped and not copied in the destination file
import re
with open("A:\\python\\chapter7\\examples\\example.py","r") as file1:
    with open("A:\\python\\chapter7\\examples\\second.py","w") as file2:
            num=1
            while True:
                buf=file1.readline()
                if len(buf)!=0:
                    buf=re.sub(r'#.+',"",buf)
                    buf=str(num)+" "+buf
                    file2.write(buf)
                    num+=1
                else:
                    break
print("File copied")

file_name=input("Enter the file name: ")
with open("A:\\python\\chapter7\\examples\\"+file_name,"r") as file1:
    text=file1.read()
    letter=input("Enter the character to be searched: ")
    count=0
    for i in text:
        if i==letter:
            count+=1
print(letter,"appears",count,"times in a file")
