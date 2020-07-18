try:
    raise Exception('Hello','World')
    #the argument would be printed after being raised
except ValueError:
    print("Value Error") 