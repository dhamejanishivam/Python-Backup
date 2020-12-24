from tkinter import *
from PIL import Image

root = Tk()
root.geometry("300x200")

def quit_1():
	quit(	)

def new():
	global i
	top = Toplevel()
	i = PhotoImage(file="u.png")
	l = Label(top,image=i)
	b = Button(top , text="Close" , command=quit_1,bg="white",fg="black")
	b.grid(row=0,column=4)
	l.grid(row=0,column=0,columnspan=3)

Button(root,text="Click",command=new).grid()

e = Stri
root.mainloop()
