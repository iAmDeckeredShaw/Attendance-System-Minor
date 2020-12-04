from tkinter import *
t = Tk()
t.geometry('400x400')

f1 = Frame()
f1.place(x=0,y=0,width=400,height=400)
def login():
	f2 = Frame()
	f2.place(x=0,y=0,width=400,height=400)
	e1 = Entry(f2)
	e1.pack()
	e2 = Entry(f2)
	e2.pack()
	b2 = Button(f2,text='Login')
	b2.pack()	



b1 = Button(f1,text='Click', command=login)
b1.pack()

t.mainloop()