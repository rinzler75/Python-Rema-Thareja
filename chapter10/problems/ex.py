class One:
    def __method(self):
        print("1")
class Two(One):
    def __method(self):
        print("2")
T=Two()
T.method()