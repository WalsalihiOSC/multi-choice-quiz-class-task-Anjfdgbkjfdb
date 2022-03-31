#week 9 multi choice task
from tkinter import*

class Multi:
    def __init__(self, parent):

        Label(parent,text="Q1. What colour does yellow and red make?").grid()

        self.select=StringVar()
        self.select.set(0)
        ans = ['Purple', 'Blue', 'Orange','Green']
        for item in ans:
            userinput=Radiobutton(text=item,value=item,variable=self.select, command=self.check)
            userinput.grid()
        self.text=Label(parent,text="")
        self.text.grid()

    def check(self):
        if self.select.get() == "Orange":
            self.text.configure(text="correct")
            self.text.grid()
        else:
            self.text.configure(text="incorrect")
            self.text.grid()


if __name__ == "__main__":        
    root = Tk()
    Multi(root)
    root.mainloop()