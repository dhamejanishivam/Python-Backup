from tkinter import *
from os import getcwdb
import tkinter.messagebox as tm

root = Tk()
root.title(getcwdb())
root.geometry("600x400")
def do():
    a=myslider2.get()
    print(f"{a} $ have been credited to your bank account")
    tm.showinfo("Your order",f"{a} $ have been credited to your bank account")

# myslider = Scale(root,from_=0,to=400)
# myslider.pack(padx=550)
Label(root,text="How many dollars($) do you want ? ").pack()
myslider2 = Scale(root,from_=0,to=300, orient=HORIZONTAL,tickinterval=150)
# myslider2.set(10)
myslider2.pack()
Button(root,text="Click Here",font="comicsansms 10 bold",command=do).pack()



root.mainloop()


