from tkinter import *
from PIL import Image

root = Tk()
root.geometry("600x400")

image_1 = PhotoImage(file="u.png")
i_l = Label(image=image_1)
i_l.grid()

root.mainloop()



