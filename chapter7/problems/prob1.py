with open("A:\\python\\chapter7\\examples\\file1.txt","r") as file1:
    with open("A:\\python\\chapter7\\problems\\file1.txt","w") as file2:
        buf=file1.readlines()
        str=buf[::-1]
        file2.writelines(str)

        print("Reversing Done...")