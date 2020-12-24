from tkinter import *
from tkinter import filedialog


root = Tk()
root.geometry("400x300")





def open():
	global i
	root_filemame = filedialog.askopenfilename(initialdir="d:/downloads",title="File",filetypes=(("png files", "*.png"),("all file" , "*.*")))
	l = Label(root , text=root_filemame)
	l.grid()
	i = PhotoImage(file=root_filemame)
	l_1 = Label(root,image=i)
	l_1.grid()


b = Button(root,text="Open file",command=open)
b.grid()



root.mainloop()

