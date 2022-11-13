from tkinter  import *
root=Tk()
root.geometry("300x400")

def Sum ():
    a.delete(0,END)
    a.insert(END,int(enterNum1.get())+int(enterNum2.get()))
    
def mine ():
    a.delete(0,END)
    a.insert(END,int(enterNum1.get())-int(enterNum2.get()))
    

Label(root,text='enterNum1 :').pack()
enterNum1 = Entry(root)

enterNum1.pack()
Label(root,text='enterNum1 :').pack()
enterNum2 = Entry(root)
enterNum2.pack()
s=Button(root , text='+',command=Sum)
s.pack()
m=Button(root , text='-',command=mine)
m.pack()
a=Listbox(root)
a.pack()

root.mainloop()