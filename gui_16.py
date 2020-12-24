from tkinter import *

from os import getcwdb

root = Tk()
root.title(getcwdb())
root.geometry("600x400")

def for_l():
    global a
    for i in range(1000):
        lsd.insert(END,f"{a}")
        a += 1

scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)

# lsd = Listbox(root, yscrollcommand= scrollbar.set)
# lsd.pack(fill="both",pady=100)
# scrollbar.config(command=lsd.yview)

text = Text(root,yscrollcommand= scrollbar.set,pady=190)
text.pack(fill="both")
scrollbar.config(command=text.yview)
# Button(root,text="Click Here",command=for_l()).pack()
# a = 1
# for i in range(1000):
#     lsd.insert(END,f"{a}")
#     a += 1



root.mainloop()


