#week 9 multi choice task
from tkinter import*

class Multi:
    def __init__(self, parent):
        data.setup(self)

        Label(parent,text="Q1. What colour does yellow and red make?").grid(row=1,column=1,columnspan=3)
        for item in data.ans:
            userinput=Radiobutton(text=item,value=item,variable = data.select, width=25,command=data.check)
            userinput.grid(column=2)
        Multi.text=Label(parent,text="")
        Multi.text.grid(row=6,column=2)


class data:
    def setup(self):
        data.ans = ['Purple', 'Blue', 'Orange','Green']
        data.select=StringVar()
        data.select.set(0)


    def check():
        if data.select.get() == "Orange":
            Multi.text.configure(text="Correct")
            Multi.text.grid()
        else:
            Multi.text.configure(text="Incorrect")
            Multi.text.grid()


root = Tk()
Multi(root)
root.mainloop()