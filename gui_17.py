from tkinter import *
import os
import tkinter.messagebox as tm
import pyperclip as py
import time



root = Tk()
root.geometry("600x400")
root.title(os.getcwdb())

def upload():
    statusvar.set("Busy ...")
    sbar.update()
    time.sleep(2)
    # print("")
    statusvar.set("Ready")


statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root , textvariable=statusvar,anchor="w")
sbar.pack(side=BOTTOM,fill="x")


Button(root, text="upload",command=upload).pack()

root.mainloop()