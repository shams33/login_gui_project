from tkinter import*


import webbrowser

root=Tk()
root.maxsize(350,500)
root.minsize(350,500)
s= StringVar()

e=Entry(root,textvariable=s,width="60").pack()
button = Button(root, text='login', fg='blue', bg='white', command=lambda: url())
button.pack()
root.mainloop()

def url(self):
     webbrowser.open_new_tab(s.get())
