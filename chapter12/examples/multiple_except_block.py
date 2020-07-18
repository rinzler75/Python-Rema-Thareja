try:
    num=int(input("Enter the number: "))
    print(num**2)
except (KeyboardInterrupt):
    print("You should have entered a number......Program Terminating...")
except (ValueError):
    print("Please check before you enter....Program Terminating....")
print("Bye")
