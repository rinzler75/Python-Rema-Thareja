import sys
with open("A:\\python\\chapter7\\problems\\"+sys.argv[1],'w') as file3:
    file3.write(" ")

with open("A:\\python\\chapter7\\problems\\"+sys.argv[1],'a') as file3:
    with open("A:\\python\\chapter7\\problems\\"+sys.argv[2],'r') as file2:
        with open("A:\\python\\chapter7\\problems\\"+sys.argv[3],'r') as file1:
            text1=file2.read()
            file3.write(text1)
            text2=file1.read()
            file3.write(text2)