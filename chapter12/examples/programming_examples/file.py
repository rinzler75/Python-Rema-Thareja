try:
    with open('A:\\python\\chapter12\\examples\\programming_examples\\myfile.txt','w') as file:
        file.write("Hello , Good Morning !!!")
except IOError:
    print("Error working with file")
else:
    print("File writting successful")