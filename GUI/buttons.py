from tkinter import Tk,Button
root=Tk()
#exit windows will close the GUI window when clicked
exitButton=Button(root,text='Exit Program',command=root.destroy)
exitButton.pack()
#to write the message on the screen and not on GUI window
def my_callback():
    print("You clicked the message button.....")
msg_button=Button(root,text='Click here',command=my_callback)
msg_button.pack()
root.mainloop()