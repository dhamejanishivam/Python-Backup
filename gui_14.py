from tkinter import *
import os


root = Tk()
root.title(os.getcwdb())
root.geometry("600x400")
a = 0
def add():
    global a
    lbx.insert(ACTIVE,f"{a}")
    a+=1

lbx = Listbox(root)
lbx.pack()
lbx.insert(END," First item of listbox")

Button(root , text="Add", command =add).pack()

root.mainloop()