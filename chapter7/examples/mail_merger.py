#mail merger consists of two files and one file contains the message which has to be sent 
#while another contains the name of the contacts whom this has to be sent
with open("A:\\python\\chapter7\\examples\\Names.txt",'r') as Names:
    with open("A:\\python\\chapter7\\examples\\Body.txt",'r') as Body:
        text=Body.read()
        for name in Names:
            msg="Hello "+name+text
            with open("A:\\python\\chapter7\\examples\\"+name.strip()+".txt",'w') as File:
                File.write(msg)