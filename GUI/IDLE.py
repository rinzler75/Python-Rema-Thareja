from tkinter import Tk,Entry,Button,INSERT
root=Tk()
#create an entry box
entry=Entry(root)
entry.pack()
#print the contents of entry box in console
def printMsg(): #text field
    print(entry.get())
button=Button(root,text='Print Content',command=printMsg)
button.pack()
root.mainloop()