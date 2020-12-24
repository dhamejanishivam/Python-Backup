from tkinter import *

def c_1():
    print("All running")

root = Tk()

root.geometry("500x500")

f_1 = Frame(root , borderwidth=6 , relief=SUNKEN )
f_1.pack(side="top" , fill="both" , anchor = "w" )

b_1 = Button(f_1 , fg="red" , text="Text" , command=c_1)
b_1.pack()

b_2 = Button(f_1 , fg="red" , text="Text")
b_2.pack()

b_3 = Button(f_1 , fg="red" , text="Text")
b_3.pack()

b_4 = Button(f_1 , fg="red" , text="Text")
b_4.pack()

f_2_3 = Entry(f_1)
f_2_3.pack()

# l_1 = Label(f_1,text="Project   Pycharm" )
# l_1.pack()

root.mainloop()