from tkinter import *

def getv():
    print(a_i.get())


root = Tk()
root.geometry("500x500")

a = Label(root , text="Username")
b = Label(root , text="Password")
a.grid()
b.grid()

a_value = StringVar()
b_value = StringVar()

a_i = Entry(root , textvariable=a_value)
b_i = Entry(root , textvariable=b_value)

a_i.grid(row=0 , column=1)
b_i.grid(row=1 , column=1)

b_1 = Button(text="Submit" , command=getv)
b_1.grid()

root.mainloop()

