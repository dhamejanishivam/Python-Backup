from tkinter import *
from PIL import Image , ImageTk


sd_root = Tk()

# geomatry input = "widhtxheight"
sd_root.geometry("500x500")

# min_size input = width,height , same is for max_size
sd_root.minsize(500,500)
# sd_root.maxsize(500,500)

# l = Label(text="Hi , I am Shivam")
# l.p1ack()

# Image insert =

photo = PhotoImage(file="u.png")
l2 = Label(image = photo)
l2.pack()

# Image inserter ends here.

# For jpg image =

# image =  Image.open("1.jpg")
# photo = ImageTk.PhotoImage(image)
# l_image = Label(image=photo)
# l_image.pack()

# Jpg image ends here.


sd_root.mainloop()