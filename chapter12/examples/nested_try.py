try:
    print("Dividing string")
    try:
        quo='abc'/'def'
    finally:
        print("In finally block.....")
except TypeError:
    print("In except Block... Handling TypeError")