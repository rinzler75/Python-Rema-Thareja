from tkinter import Tk, Label
root=Tk()
label=Label(root,text='Message printing label.....')
label.pack()
def my_callback():
    print("Welcome to GUI programming of Python")
label.bind('<Button-1>',lambda e:my_callback())
root.mainloop()