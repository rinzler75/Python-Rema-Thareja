import sys
from tkinter import Tk,Label,PhotoImage
root=Tk()
img=PhotoImage(file='A:\\pictures\\aunty.jpg')
IMG=Label(root,image=img)
IMG.pack()
root.mainloop()
