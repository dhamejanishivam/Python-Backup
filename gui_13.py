from tkinter import *
import os
import tkinter.messagebox as tm


root = Tk()
root.geometry("600x400")
root.title(os.getcwdb())
var = IntVar()
def order():
    ab = var.get()
    if ab==1:
        abc="Dosa"
    elif ab==2:
        abc="Vada-Pav"
    else: abc="Samosa"
    tm.showinfo("Order", f"We have placed your order for {abc} ")


Label(root, text="What would you like to have sir!", justify = LEFT,font="lucida  11 bold").pack(pady=20)
radio = Radiobutton(root , text="Dosa",variable=var,value=1)
radio.pack(anchor="w",padx=50,pady=20)

radio1 = Radiobutton(root , text="Vada-Pav",variable=var,value=2)
radio1.pack(anchor="w",padx=50,pady=20)

radio2 = Radiobutton(root , text="Samosa",variable=var,value=3)
radio2.pack(anchor="w",padx=50,pady=20)

button = Button(text="Order now",command=order)
button.pack()

root.mainloop()