try:
    print("Raising Exception....")
    raise ValueError
except:
    print("Exception Caught")
finally:#it has to come after the except statement
    print("Performing clean up in Finally....")