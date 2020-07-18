try:
    raise NameError
except:
    print("Re raising the exception")
    #the exception is re raised
    raise