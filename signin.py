from tkinter import *


root = Tk()
root.geometry("300x400")



Label(root,text="Name : ").pack()
name=Entry(root)
name.pack()
Label(root,text="Family : ").pack()
family=Entry(root)
family.pack()
Label(root,text="Email : ").pack()
email=Entry(root)
email.pack()
Label(root,text="password : ").pack()
password=Entry(root , show='*')
password.pack()

root.mainloop()