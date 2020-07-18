from tkinter import Tk,Label
root=Tk()
label=Label(root,text='welcome to the gui programming in python !!!')
label.pack()
label.config(foreground='yellow',background='blue',text='updated text')
root.mainloop()