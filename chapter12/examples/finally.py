try:
    print("Raising Exception")
    raise ValueError
finally: #re raises the exception after the , execution of the finally block
    print("Performing clean up in the finally")