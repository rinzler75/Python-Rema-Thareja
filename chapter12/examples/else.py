try:
    num=int(input("Enter the number: "))
    print(num**2)
except (ValueError):
    print("Please check before you enter....Program Terminating....")
#if no exception is caught
else:
    print("Program terminating successfully......")
