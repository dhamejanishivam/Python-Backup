from tkinter import *


root = Tk()
width = 600
height = 500
def change_val():
    global width
    width = int(var_1.get())
    global height
    height = int(var_2.get())
    root.geometry(f"{width}x{height}")

root.geometry(f"{width}x{height}")

heading = Label(root , text="Window Resizer",font="comicsansms 16 bold")
heading.grid(row=0,column=4)

l_w = Label(root, text="Enter Width",font="comicsansms 15")
l_h = Label(root,text="Enter Height",font="comicsansms 15")

var_1 = IntVar()
var_2 = IntVar()

inp_1 = Entry(root, textvariable=var_1)
inp_2 = Entry(root, textvariable=var_2)

b_1 = Button(root , text="Click Here",font="comicsansms 12 bold",command=change_val)



l_w.grid(row=2,column=2,pady=50)
l_h.grid(row=3,column=2)
inp_1.grid(row=2,column=8)
inp_2.grid(row=3,column=8)
b_1.grid(pady=50,row=7,column=8)

root.mainloop()