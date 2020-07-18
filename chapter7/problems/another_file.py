 
 
 
with (open("A:\\python\\chapter\\examples\\file.txt","r")) as file: 
    line=file.read()
    words=line.split()
    print(words)