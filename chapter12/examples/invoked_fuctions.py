def Divide(num,deno):
    try:
        quo=num/deno
    except ZeroDivisionError:
        print("You cannot divide a number by zero.....Program Terminating.....")
Divide(10,0)
