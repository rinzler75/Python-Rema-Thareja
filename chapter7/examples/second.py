1 
2 
3 
4 with (open("A:\\python\\chapter7\\examples\\file1.txt","r")) as file1: 
5     line=file1.read()
6     words=line.split()
7     print(words)