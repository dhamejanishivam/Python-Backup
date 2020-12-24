from tkinter import *
from PIL import Image , ImageTk
import os


root = Tk()

root.geometry("655x333")

f_1 = Frame(root , bg="grey" , borderwidth=6 , relief=SUNKEN )
f_1.pack(side="top" , fill="both" , anchor = "w" , padx=273)

f_2 = Frame(root , bg="grey" , borderwidth=6 , relief = SUNKEN)
f_2.pack(side="left" , fill="both" , anchor="w" , pady=100)

l_1 = Label(f_1,text="Project   Pycharm" )
l_1.pack()

l_2 = Label(f_2 , text="Files - ")
l_2.pack()


root.mainloop()