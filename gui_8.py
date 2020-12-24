from tkinter import *
from selenium import webdriver
from time import *


root = Tk()
root.title("gui_8")

canvas_width = 700
canvas_height = 600

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()


# This line goes from the point (x,y) to (x1,y1)
# can_widget.create_line(0,0,700,600 , fill="red")
# can_widget.create_line(0,600,700,0 , fill="red")


# Rectangle coordinat to input = topleft(x,y) , bottomright(x1,y1)
# can_widget.create_rectangle(4,4,696,596,fill="blue")

# Create text
# can_widget.create_text(60,40 , text="Python", font="comicsansms 19 bold")

# Create Oval -
# can_widget.create_oval(50,60,400,450)

img = PhotoImage(file="u.png")
can_widget.create_image(2,20,image=img)

root.mainloop()