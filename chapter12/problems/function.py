name=''
def kumar():
   
        global name
        name=int(input("Enter the name: "))
def dis():
    try:
        kumar()
    except:
        print("Wrong input")
    print(name)

dis()
