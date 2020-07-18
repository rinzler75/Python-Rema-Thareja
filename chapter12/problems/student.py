name=''
roll=0
def readData():
    global name,roll
    name=input('Enter name: ')
    roll=int(input("Enter roll: "))
def display():
    print("NAME: ",name)
    print("Roll: ",roll)

flag=True
while(flag):
    try:
        readData()
        flag=False
    except(KeyboardInterrupt,TypeError,ValueError):
        print("Wrong input enter the data again: ")
        
display()