from tkinter import *


root = Tk()
root.geometry("300x400")



Label(root,text="Name : ").pack()
name=Entry(root)
name.pack()
Label(root,text="Family : ").pack()
family=Entry(root)
family.pack()

root.mainloop()