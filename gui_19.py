from tkinter import *


root = Tk()
root.geometry("600x400")
root.title("Gui_19")
root.wm_iconbitmap("notepad.ico")
root.configure(bg="pink")


w = root.winfo_screenwidth()
h = root.winfo_screenheight()
print(w,h)


Button(root , text="Close" , command=root.destroy).pack()

root.mainloop()
