from tkinter import messagebox
title='Customer Feedback'
text='Did u like our customer service'
reply=messagebox.askquestion(title,text)
if reply=='Yes':
    print("Thank you very much....")
else:
    print("We regret the inconvinience. Please give us another chance")