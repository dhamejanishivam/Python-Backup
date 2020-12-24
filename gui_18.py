from tkinter import *

a = "999999"

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self , textvariable=self.var, anchor="w")
        self.statusbar.pack(side=BOTTOM,fill=X)

    # inp_1 = StringVar()
    # Entry(self , textvariable=inp)
    def click(self):
        pass
    def createbutton(self , text):
        Button(text=text , command=self.click).pack()


if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createbutton("MC")
    window.mainloop()

