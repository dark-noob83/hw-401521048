from tkinter  import *
root=Tk()
root.geometry("300x400")

def Sum ():
    a.delete(0,END)
    a.insert(END,float(enterNum1.get())+float(enterNum2.get()))
    
def mine ():
    a.delete(0,END)
    a.insert(END,float(enterNum1.get())-float(enterNum2.get()))
def multi ():
    a.delete(0,END)
    a.insert(END,float(enterNum1.get())*float(enterNum2.get()))
def devide ():
    a.delete(0,END)
    a.insert(END,float(enterNum1.get())/float(enterNum2.get()))

def pow ():
    a.delete(0,END)
    a.insert(END,float(enterNum1.get())**float(enterNum2.get()))  

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
zarb=Button(root , text='*',command=multi)
zarb.pack()
tagh=Button(root , text='/',command=devide)
tagh.pack()
power=Button(root , text='power',command=pow)
power.pack()
a=Listbox(root)
a.pack()

root.mainloop()