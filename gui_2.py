from tkinter import *
from PIL import Image , ImageTk
import os

sd_root = Tk()

# geomatry input = "widhtxheight"
sd_root.geometry("500x500")

# min_size input = width,height , same is for max_size
sd_root.minsize(500,500)
# sd_root.maxsize(500,500)


# This change top-left title of gui
sd_root.title(os.getcwdb())


""" Label attributes = 
text = add the text
bd = background
fg = foreground
font = set the font
two ways of font are =
        1. font = font =("comicsansms" , 14 , "bold")
        2.fnt = font = "comicsansms 14 bold"
padx = xpading
pady = ypading
relief = border style
"""

l_1 = Label(text="""Best Hindi Videos For Learning Programming:


""" , bg = "red" , fg = "white" , font = "comicsansms 14 bold" , borderwidth = "3" , relief = SUNKEN            )


""" Pack attributes = 

anchor = "nw" , nw = is a dirction we can write any direction
side = top , bottom , left , right
fill = fill function strech the gui
padx = fill space between text and border
pady = same as padx but in other direction


"""

l_1.pack(side="top" , anchor = "center" ,fill="both",padx="0",pady="0" )

sd_root.mainloop()