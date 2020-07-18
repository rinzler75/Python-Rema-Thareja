class Iterator:
    def __init__(self, string):
        self.string=string
        self.index=0
    def __iter__(self): #here we have defined our own iterator as u can see over here
        return self
    def __next__(self): #and the next function also which we have defined 
        if self.index>=len(self.string):
            raise StopIteration # same like throw in java
        string=self.string[self.index]
        self.index+=1
        return string
it = Iterator("Hello World") 
for char in it:
    print(char,end=" ")
