from tkinter import *
from os import getcwdb

root = Tk()
root.geometry("600x400")
root.title(getcwdb())
def myfunc():
    print("Hello")


# Function menu
# mymenu = Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)


# Menubar menu -
yourmenubar = Menu(root)
m1 = Menu(yourmenubar , tearoff=0)
m1.add_command(label="Print",command=myfunc)
m1.add_separator()
m1.add_command(label="Exit", command=quit)
yourmenubar.add_cascade(label="File",menu=m1)
root.config(menu=yourmenubar)



m2 = Menu(yourmenubar , tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_separator()
m2.add_command(label="Copy", command=quit)
yourmenubar.add_cascade(label="Edit",menu=m2)
root.config(menu=yourmenubar)





root.mainloop()

