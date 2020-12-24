from  tkinter import *

ans = 0
root = Tk()
root.title("Calculator")
root.geometry("500x350")
root.configure(bg="white")
root.maxsize(500,350)
root.minsize(500,350)
root.config(bg="white") 
e = Entry(root,bg="grey97",width=55,relief=SUNKEN,font="comicsansmm 15")
op = 0
def click(number):
    e.insert(END , number)
def add():
    e.get()
    global first_num , op 
    op = 1
    first_num = e.get()    
    e.delete(0 , END)
def sub():
    global first_num , op
    op = 2
    first_num = e.get()
    e.delete(0 , END)
def mul():
    global first_num , op
    op = 3
    first_num = e.get()
    e.delete(0 , END)
def div():
    global first_num , op
    op = 4
    first_num = e.get()
    e.delete(0 , END)    
def equal():
    global secod_num
    secod_num = e.get()
    if op==1 :
        result =  float(first_num)+float(secod_num)
    elif op==2 :
        result =  float(first_num)-float(secod_num)
    elif op==3 :
        result =  float(first_num)*float(secod_num)
    elif op==4 :
        result = float(first_num)/float(secod_num)
    else :
        print("Eror")
    e.delete(0 , END)
    e.insert(0 , result)   
l_1 = Label(root , bg="white",text="Function - " , font="comicsansms 12 bold")
b_1 = Button(root, text="1" ,width=10,font="comicsansms 12 " ,command=lambda : click(1))
b_2 = Button(root, text="2" ,width=10,font="comicsansms 12 ",  command=lambda : click(2))
b_3 = Button(root, text="3" ,width=10,font="comicsansms 12 " , command=lambda : click(3))
b_4 = Button(root, text="4" ,width=10,font="comicsansms 12 " , command=lambda : click(4))
b_5 = Button(root, text="5" ,width=10,font="comicsansms 12 " , command=lambda : click(5))
b_6 = Button(root, text="6" ,width=10,font="comicsansms 12 " ,command=lambda : click(6))
b_7 = Button(root, text="7" ,width=10,font="comicsansms 12 " , command=lambda : click(7))
b_8 = Button(root, text="8" ,width=10,font="comicsansms 12 " , command=lambda : click(8))
b_9 = Button(root, text="9" ,width=10,font="comicsansms 12 " , command=lambda : click(9))
b_0 = Button(root, text="0" ,font="comicsansms 12 " ,padx=40, command=lambda : click(0))
b_dot = Button(root, text="." ,font="comicsansms 12 ",bg="black",fg="white" ,padx=40, command=lambda : click("."))
# 
b_add = Button(root, text="+" ,font="comicsansms 12 " ,padx=40, command=add)
b_sub = Button(root, text="-" ,font="comicsansms 12 " ,padx=40, command=sub)
b_mul = Button(root, text="x" ,font="comicsansms 12 " ,padx=40, command=mul)
b_div = Button(root, text="/" ,font="comicsansms 12 " ,padx=40, command=div)
# 
b_equal = Button(root, bg="black",fg="white",text = "=" ,font="comicsansms 12 " ,padx=40, command=equal)
# 
e.grid(row=0,columnspan=6)
Label(root,bg="white",text="").grid(row=2,columnspan=6)
b_1.grid(row=3,column=0,pady=5)
b_2.grid(row=3,column=1)
b_3.grid(row=3,column=2)
b_4.grid(row=4,column=0,pady=5)
b_5.grid(row=4,column=1)
b_6.grid(row=4,column=2)
b_7.grid(row=5,column=0,pady=5)
b_8.grid(row=5,column=1)
b_9.grid(row=5,column=2)
b_0.grid(row=6,column=1,pady=10)
b_dot.grid(row=6,column=2)
# 
l_1.grid(row=7,column=0)
b_add.grid(row=8,column=0,pady=10)
b_sub.grid(row=8,column=1,pady=10)
b_mul.grid(row=9,column=0,pady=10)
b_div.grid(row=9,column=1,pady=10)
# 
b_equal.grid(row=6,column=0,pady=5)
# 
root.mainloop()
