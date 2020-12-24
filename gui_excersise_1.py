from tkinter import *

news_root = Tk()

news_root.geometry("500x500")

image_1 = PhotoImage(file="u.png")
image_1_pack = Label(image=image_1 , bg="white")
image_1_pack.pack(side=RIGHT , anchor="nw")

news_root.mainloop()