class Counter():
    val=0
    def __iter__(self):
        return self
    def __next__(self):
        val=self.val
        self.val+=1
        return self.val
c=Counter()
while True:
    print(c.__next__()) #its an infinite loop