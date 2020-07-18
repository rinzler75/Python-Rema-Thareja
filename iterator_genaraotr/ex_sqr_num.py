class Square:
    def __init__(self):
        self.val=0
    def __iter__(self):
        return self
    def __next__(self):
        self.val+=1
        return self.val**2
Sq=Square()
count=0
for num in Sq: #do remember here sq becomes ur iterator and u cant call the value using some input for loop Sq will help
    print(num,end=' ')
    if count==10:
        break
    count+=1


        