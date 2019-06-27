from tkinter import *

class calculator:

    def __init__(self):


        self.root = Tk()

        self.root.title('login')

        self.root.minsize(250, 350)
        self.root.maxsize(250, 350)
        self.result=Label(self.root,text='',bg='white',width=6,height=4)
        self.result.grid(row=0,coloumn=0)
        self.root.mainloop()