#this is the comment part 
#comment

with (open("A:\\python\\chapter7\\examples\\file1.txt","r")) as file1: #comment
    line=file1.read()
    words=line.split()
    print(words)