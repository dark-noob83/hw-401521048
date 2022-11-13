from tkinter  import *
root=Tk()
root.geometry("300x400")

Label(root,text='enterNum1 :').pack()
enterNum1 = Entry(root)

enterNum1.pack()
Label(root,text='enterNum1 :').pack()
enterNum2 = Entry(root)
enterNum2.pack()


root.mainloop()