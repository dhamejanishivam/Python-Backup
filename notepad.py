from tkinter import *
import os
import tkinter.messagebox as tm
import pyperclip as py
import time



def notepad_main():
    style = "comicsansms"
    size = "12"
    bold = ""


    root = Tk()
    root.wm_iconbitmap("notepad.ico")
    root.title(f"Notepad ")
    root.geometry("800x600")




    def update():
        text = Text(bg="white", font=f"{style} {size} {bold}")
        text.update()

    def copy():
        a = text.get("1.0","end")
        py.copy(a)
    def quit_1():
        quit()

    def paste():
        text.insert(END,f"\n{py.paste()}")
    def save_2():
        global var_1, ab
        # var_1 = StringVar()
        Entry(root, textvariable=var_1).grid()
        Button(root,text="Save",command=save).grid()

    def save():
        # var_1 = StringVar()
        global var_1,ab
        # ab = var_1.get()
        ab = var_1.get()
        print(ab)
        a = text.get("1.0", "end")
        with open(f"{ab}.txt", "w") as f:
            f.write(a)
        tm.showinfo("Save", f"Notepad saved as {ab}.txt ")

    def warning():
        tm.showerror("Warning","You are not allowed to acess source code, Contact Shivam for further help")
    def support():
        tm.showinfo("Help and Support" , "Please contact Shivam \n"
                                        "Mobile no. = 9644971120  \n"
                                        "Email = dhamejanishivam@gmail.com")
    def copy_c_d():
        py.copy("9644971120 , dhamejanishivam@gmail.com")
        tm.showinfo("Work done" , "Contact details are copied")


    # Menu -
    main_m = Menu(root)
    m1 = Menu(main_m,tearoff=0)
    m1.add_command(label="Exit",command=quit_1)
    m1.add_command(label="Copy",command=copy)
    m1.add_command(label="Paste",command=paste)
    m1.add_command(label="Save",command=save_2)
    root.config(menu=main_m)
    m2 = Menu(main_m,tearoff=0)
    m2.add_command(label="View Code",command=warning)
    m3 = Menu(main_m,tearoff=0)
    m3.add_command(label="Support",command=support)
    m3.add_command(label="Copy contact details",command=copy_c_d)
    m4 = Menu(main_m,tearoff=0)
    m4.add_command(label="Edit font" )
    m4.add_command(label="Update",command=update)
    main_m.add_cascade(label="File",menu=m1)
    main_m.add_cascade(label="View",menu=m2)
    main_m.add_cascade(label="Support",menu=m3)
    # main_m.add_cascade(label="Font",menu=m4)
    # Ends Here


    # Text code -
    text = Text(bg="white",font = f"{style} {size} {bold}")
    text.grid(row=0,column=0,columnspan=4, sticky = N+S+E+W)
    root.grid_columnconfigure(0 , weight=1)
    root.grid_rowconfigure(0 , weight=1)
    root.mainloop()
    # Ends Here

if __name__ == "__main__":
    notepad_main()