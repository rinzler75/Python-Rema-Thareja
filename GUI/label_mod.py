from tkinter import Tk,Message
root = Tk()
msg=Message(root,text='Welcome to tkinter programming!!!')
msg.config(font=('monaco',15,'bold underline'))

msg.pack()
root.mainloop()