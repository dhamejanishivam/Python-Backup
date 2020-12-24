from tkinter import *

root = Tk()

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0


def getv():
    print("Submiting Form")
    print(f"{name_v.get(),phone_v.get(),gender_v.get(),emergency_v.get(),payment_v.get(),food_service_checkbox.get()}")

    with open("records.txt" , "a") as f:
        f.write(f"{name_v.get(),phone_v.get(),gender_v.get(),emergency_v.get(),payment_v.get(),food_service_checkbox.get()} \n")


root.geometry("500x500")

l_1 = Label(root , text="Welcome to shivam travel" , font="comicnsansms 13 bold")
l_1.grid(row=0 , column=3)

name = Label(root , text="Name")
phone = Label(root , text="Phone")
gender = Label(root , text="gender")
emergeny_no = Label(root , text="number")
paymet = Label(root , text="payment")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergeny_no.grid(row=4,column=2)
paymet.grid(row=5,column=2)

name_v = StringVar()
phone_v = StringVar()
gender_v = StringVar()
emergency_v = StringVar()
payment_v = StringVar()
food_service_checkbox = IntVar()

name_e = Entry(root , textvariable=name_v).grid(row= 1, column=3)
phone_e = Entry(root , textvariable=phone_v).grid(row=2 , column=3)
gender_e = Entry(root , textvariable=gender_v).grid(row=3 , column=3)
emergency_e = Entry(root , textvariable=emergency_v).grid(row=4 , column=3)
payment_e = Entry(root , textvariable=payment_v).grid(row= 5, column=3)

# CheckBox -
food_checkbox = Checkbutton(text="Want to prebook your meals" , variable=food_service_checkbox)
food_checkbox.grid(row=6 , column=3)

#  Button -

Button(text="Sumbit form" , command=getv).grid(row=7,column=3)


root.mainloop()


# print(f"{a}\n {b} \n {c} \n {d} \n {e} \n {f} \n")