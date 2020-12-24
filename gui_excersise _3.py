from tkinter import *
import tkinter.messagebox as tm


root = Tk()
root.geometry("600x400")
def bt():
    ac = a.get()
    if ac<=5:
        tm.showinfo("Feedback","Sorry to see that your experince was not good")
    elif ac>5:
        tm.showinfo("Feedback", "Glad tho hear that please rate us on app store")
Label(root , text="You ordered food from us , Please rate us on this slide bar").pack()
a = Scale(root, from_=0,to=10,orient=HORIZONTAL)
a.set(10)
a.pack()
b = Button(root , text="Click Here",command=bt).pack()


root.mainloop()

