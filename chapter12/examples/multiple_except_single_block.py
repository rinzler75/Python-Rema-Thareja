try:
    num=int(input("Enter the number: "))
    print(num**2)
except (KeyboardInterrupt,ValueError,TypeError):
    print("You should have entered a number......Program Terminating...")
print("Bye")
