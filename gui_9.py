from tkinter import *

root = Tk()
root.geometry("600x550")
def sd(event):
    print(f"Cliked at {event.x},{event.y}")


widget = Button(root , text="Click me")
widget.pack()

# widget.bind('<Button-1>',sd)
widget.bind('<Double-1>',quit)

root.mainloop()