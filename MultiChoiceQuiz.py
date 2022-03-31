#week 9 multi choice task
from tkinter import*

class Multi:
    def __init__(self, parent):

        Label(parent,text="Q1. What colour does yellow and red make?").grid()

        self.select=StringVar()
        self.select.set(0)
        ans = ['Purple', 'Blue', 'Orange','Green']
        for item in ans:
            Radiobutton(text=item,value=item,variable=self.select).grid(padx=10)
        
        

        


if __name__ == "__main__":        
    root = Tk()
    Multi(root)
    root.mainloop()