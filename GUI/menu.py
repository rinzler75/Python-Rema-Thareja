from tkinter import Tk,Menu
root=Tk()
#create main menu bar
menu_bar=Menu(root)
fileMenu=Menu(menu_bar,tearoff=0)
fileMenu.add_command(label='Stop',command=root.destroy)
fileMenu.add_command(label='Kill',command=root.destroy)
fileMenu.add_command(label='Exit',command=root.destroy)
menu_bar.add_cascade(label='File',menu=fileMenu)
root.config(menu=menu_bar)
root.mainloop()