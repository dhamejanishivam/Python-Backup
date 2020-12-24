from tkinter import *
from selenium import webdriver
from time import *




root = Tk()
root.title("Music downloader")
root.geometry("500x500")
root.maxsize(500,500)
root.minsize(500,500)
root.configure(bg="white")

def getv():
    a =  link_input.get()
    site = webdriver.Chrome()
    site.minimize_window()
    site.get("https://ytmp3.cc/en13/")
    b = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]")
    b.send_keys(a)
    convert_button = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[2]")
    convert_button.click()
    sleep(4)
    download_buutton = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")
    download_buutton.click()


link_label = Label(root ,text="Enter the link of song from Youtube" , fg="blue" ,font = "comicsansms 15 bold")
link_label.grid(padx =100 , pady=50)

input_l = StringVar

link_input = Entry(root , textvariable=input_l , bg="white" , font="comicsansms 18 bold" ,borderwidth=3,relief=SUNKEN,show="")
link_input.grid(padx=50 , pady =20 )


b_1 = Button(root,relief=SUNKEN , text="Click here to download" ,bg="pink",fg="red" ,font="comicsansms 15 bold" , command=getv)
b_1.grid(pady=10 )

root.mainloop()







