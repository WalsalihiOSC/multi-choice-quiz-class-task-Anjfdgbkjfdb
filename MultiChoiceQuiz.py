#week 9 multi choice task
from tkinter import*

class Multi:
    def __init__(self, parent):

        Label(parent,text="Q1. What colour does yellow and red make?").grid(row=1,column=1,columnspan=3)
        self.select=StringVar()
        self.select.set(0)
        ans = ['Purple', 'Blue', 'Orange','Green']
        for item in ans:
            userinput=Radiobutton(text=item,value=item,variable=self.select, width=25,command=self.check)
            userinput.grid(column=2)
        self.text=Label(parent,text="")
        self.text.grid(row=6,column=2)

    def check(self):
        if self.select.get() == "Orange":
            self.text.configure(text="Correct")
            self.text.grid()
        else:
            self.text.configure(text="Incorrect")
            self.text.grid()


root = Tk()
Multi(root)
root.mainloop()