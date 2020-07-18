#instatiation of the exception block
try:
    raise Exception('Hello','World')
except Exception as errorObj:
    print(type(errorObj))
    print(errorObj.args)
    print(errorObj)
    arg1,arg2=errorObj.args
    print('Argument1 = ',arg1)
    print('Argument2 = ',arg2)