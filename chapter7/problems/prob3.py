
with open("A:\\python\\chapter7\\examples\\second.py",'r') as file:
    with open("A:\\python\\chapter7\\problems\\another_file.py",'w') as file1:
        buf="sdfgsd"
        while len(buf)!=0:
            buf=file.readline()
            for i in buf:
                if i.isdigit():
                    continue
                else:
                    file1.write(i)
            

