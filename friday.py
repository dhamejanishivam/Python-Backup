from win32com.client import Dispatch
from datetime import datetime
from datetime import date
from pygame import mixer
import time
from tkinter import *
import os
from selenium import webdriver
import pyautogui as pg
import sys


now = datetime.now()
hour = now.strftime("%H")
minute = now.strftime("%M")
realtime = now.strftime("%H:%M:%S")
hour = int(hour)
minute = int(minute)


def ai(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def quit_1():
    quit()

# Time section -
if hour >= 23 :
    if minute >=30 :
        ai(f' Boss it is {hour} in  night  ')
        time.sleep(0.5)
        ai(f' you should take rest now ')
        loop_break = 0
        while (loop_break == 0) :
            ai (f' Do you still want me to proceed ')
            ai (f' Press Y for yes and N for no ')
            print(f' Press Y for yes and N for no ')
            loop_input = input()
            if loop_input=="n" or loop_input=="N":
                ai(f' Do you want me to Shut down laptop ')
                print(f'Do you want me to Shut down laptop ')
                shut_i = input 
                if shut_i=="Y" or shut_i=="y":
                    ai(f' Shutting down laptop ')
                    os.system("shutdown /s /t 1") 
                    # ai(f'Ok Boss exiting')
                    # quit_1( )
                else :  
                    print("IN else")
                    ai(f' Ok quiting ')  
                    quit_1()
            else :  loop_break+=1
    else :  ai(f' Boss it is {hour} in night ')            
elif 22<=hour<23 :
    ai(f' Welcome Boss it is {hour} hours , {minute} minutes ')


elif  16<=hour<=21 :
    ai(f' Good evening boss ')

elif  13<=hour<=15 :
    ai(f'Good afternoon boss ')

elif hour==12 :
    ai(f' Welcome Boss it is a perfect noon ')

elif  4<=hour<=11 :
    ai(f' Good morning Boss ')
elif  1<=hour<=3 :
    ai(f' Boss it is {hour} in post midnight  ')
    time.sleep(0.1)
    ai(f' You should take rest now ')
    loop_break = 0
    while (loop_break == 0) :
        ai (f' Do you still want me to proceed ')
        ai (f' Press Y for yes and N for no ')
        print(f'Press Y for yes and N for no ')
        loop_input = input()
        if loop_input=="n" or loop_input=="N":
            ai(f' Do you want me to Shut down laptop ')
            print(f'Do you want me to Shut down laptop ')
            shut_i = input()
            if shut_i=="Y" or shut_i=="y":
                ai(f' Shutting down laptop ')
                os.system("shutdown /s /t 1") 
            else :
                ai(f' Ok quiting ')  
                quit_1()
        else :  loop_break+=1

elif hour==0 :
    if minute==0:
        ai(f' Boss it is a perfect midnight ')
    elif minute<=39 :
        ai(f' Welcome Boss , it is midnight ')
    elif minute>=40 :
        ai(f' Boss it is {hour} in post midnight  ')
        time.sleep(0.1)
        ai(f' You should take rest now ')
        loop_break = 0
        while (loop_break == 0) :
            ai (f' Do you still want me to proceed ')
            ai (f' Press Y for yes and N for no ')
            print(f'Press Y for yes and N for no ')
            loop_input = input()
            if loop_input=="n" or loop_input=="N":
                ai(f' Do you want me to Shut down laptop ')
                print(f'Do you want me to Shut down laptop ')
                shut_i = input()
                if shut_i=="Y" or shut_i=="y":
                    ai(f' Shutting down laptop ')
                    os.system("shutdown /s /t 1") 
                else :
                    ai(f' Ok quiting ')  
                    quit_1()
            else :  loop_break+=1
# Time section ends here.
               


i = 1
while(True) :
    if i==1 :
        ai("What can I do for you")
        print("\n")
        print("Press 1 for to know what time it is  \n"
          "Press 2 for music playing \n"
          "Press 3 for setting alaram \n"
          "Press 4 for opening a site \n"
          "Press 5 downloding a song \n"
          "Press 6 for asking date \n"
          "Press 7 for playing Rock Paper Scisor \n"
          "Press 8 for file genrator \n"
          "Press 9 to open Notepad \n"
          "Press 10 to serch anything in Google \n"
          "Press 11 to open Calculator \n"
          "Press S for Shut down \n"
          "Press q to quit the program \n")
    else:
        ai("What else can I do for you ")
        print("\n")
        print("Enter talk for a casual talk \n"
              "Press 1 for to know what time it is  \n"
              "Press 2 for music playing \n"
              "Press 3 for setting alaram \n"
              "Press 4 for opening a site \n"
              "Press 5 downloding a song from youtube \n"
              "Press 6 for asking date \n"
              "Press 7 for playing Rock Paper Scisor \n"
              "Press 8 for file genrator \n" 
              "Press 9 to open Notepad \n"
              "Press 10 to serch anything in Google \n"
              "Press 11 to open Calculator \n"
              "Press S for Shut down \n"
              "Press q to quit the program \n")
    i = i + 1
    aa = input()
    if aa=="1" :
        ai(f"The time is {hour} hours and {minute} minutes")
    elif aa=="talk":
        ai("Enter what you want to say")
    elif aa=="2" :
        ai("Opening Music Player")

        def music_play():
            root = Tk()
            root.geometry("1000x500")
            root.configure(bg="blue")

            def quit_1():
                quit()
            def pause():
                mixer.init()
                mixer.music.pause()
            def resume():
                mixer.init()
                mixer.music.unpause()
            def s_1():
                mixer.init()
                mixer.music.load("nike_vasudev.mp3")
                mixer.music.play()
            def s_2():
                mixer.init()
                mixer.music.load("ghaziabad_vasudev.mp3")
                mixer.music.play()
            def s_3():
                mixer.init()
                mixer.music.load("drake_laugh_now.mp3")
                mixer.music.play()
            def s_4():
                mixer.init()
                mixer.music.load("gods_plan.mp3")
                mixer.music.play()
            def s_5():
                mixer.init()
                mixer.music.load("maharani.mp3")
                mixer.music.play()
            def s_6():
                mixer.init()
                mixer.music.load("awien_hai.mp3")
                mixer.music.play()
            def s_7():
                mixer.init()
                mixer.music.load("chenni_khatam.mp3")
                mixer.music.play()
            def s_8():
                mixer.init()
                mixer.music.load("mujhe_farak.mp3")
                mixer.music.play()
            def s_9():
                mixer.init()
                mixer.music.load("makasam.mp3")
                mixer.music.play()
            def s_10():
                mixer.init()
                mixer.music.load("seedha_makeover.mp3")
                mixer.music.play()
            def s_11():
                mixer.init()
                mixer.music.load("bcbeat.mp3")
                mixer.music.play()
            def s_12():
                mixer.init()
                mixer.music.load("dil.mp3")
                mixer.music.play()        
            def s_13():
                mixer.init()
                mixer.music.load("hanikarak.mp3")
                mixer.music.play()
            def s_14():
                mixer.init()
                mixer.music.load("hater.mp3")
                mixer.music.play()
            def s_15():
                mixer.init()
                mixer.music.load("ladki.mp3")
                mixer.music.play()
            def s_16():
                mixer.init()
                mixer.music.load("mujra.mp3")
                mixer.music.play()
            def s_17():
                mixer.init()
                mixer.music.load("asli.mp3")
                mixer.music.play()    
            def s_18():
                mixer.init()
                mixer.music.load("bhang.mp3")
                mixer.music.play()
            def s_19():
                mixer.init()
                mixer.music.load("harami.mp3")
                mixer.music.play()
            def s_20():
                mixer.init()
                mixer.music.load('bella.mp3')
                mixer.music.play()    

            root.title(f'Made by Shivam')
            heading = Label(root,text="Music Player",bg="black",fg="white",font="comicsansms 15 bold")
            heading.grid(column=5,pady=10)



            song_1 = Label(root,text="Nike by vasudev",bg="blue",fg="yellow",font="comicsansms 12")
            song_2 = Label(root,text="Ghaziabad",bg="blue",fg="yellow",font="comicsansms 12")
            song_3 = Label(root,text="Laugh now",bg="blue",fg="yellow",font="comicsansms 12")
            song_4 = Label(root,text="God's plan",bg="blue",fg="yellow",font="comicsansms 12")
            song_5 = Label(root,text="Maharani",bg="blue",fg="yellow",font="comicsansms 12")
            song_6 = Label(root,text="Awien hai",bg="blue",fg="yellow",font="comicsansms 12")
            song_7 = Label(root,text="Chenni Khatam",bg="blue",fg="yellow",font="comicsansms 12")
            song_8 = Label(root,text="Mujhe farak",bg="blue",fg="yellow",font="comicsansms 12")
            song_9 = Label(root,text="Makasam",bg="blue",fg="yellow",font="comicsansms 12")
            song_10 = Label(root,text="Seedha Makeover",bg="blue",fg="yellow",font="comicsansms 12")
            song_11 = Label(root,text="Bakchod Beat",bg="blue",fg="yellow",font="comicsansms 12")
            song_12 = Label(root,text="Dil ki Baat",bg="blue",fg="yellow",font="comicsansms 12")
            song_13 = Label(root,text="Hannikarak",bg="blue",fg="yellow",font="comicsansms 12")
            song_14 = Label(root,text="Haters",bg="blue",fg="yellow",font="comicsansms 12")
            song_15 = Label(root,text="Ladki Dokebaaz",bg="blue",fg="yellow",font="comicsansms 12")
            song_16 = Label(root,text="Mujra(Tik-Tok Diss)",bg="blue",fg="yellow",font="comicsansms 12")
            song_17 = Label(root,text="Asli Basad",bg="blue",fg="yellow",font="comicsansms 12")
            song_18 = Label(root,text="Bhang Bharosa",bg="blue",fg="yellow",font="comicsansms 12")
            song_19 = Label(root,text="Khamoosh Harami",bg="blue",fg="yellow",font="comicsansms 12")
            song_20 = Label(root,text="Bella Chio",bg="blue",fg="yellow",font="comicsansms 12")


            b_1 = Button(root,text="Play",font="comisansms 10 ",command=s_1)
            b_2 = Button(root,text="Play",font="comisansms 10",command=s_2)
            b_3 = Button(root,text="Play",font="comisansms 10",command=s_3)
            b_4 = Button(root,text="Play",font="comisansms 10",command=s_4)
            b_5 = Button(root,text="Play",font="comisansms 10",command=s_5)
            b_6 = Button(root,text="Play",font="comisansms 10",command=s_6)
            b_7 = Button(root,text="Play",font="comisansms 10",command=s_7)
            b_8 = Button(root,text="Play",font="comisansms 10",command=s_8)
            b_9 = Button(root,text="Play",font="comisansms 10",command=s_9)
            b_10 = Button(root,text="Play",font="comisansms 10",command=s_10)
            b_11 = Button(root,text="Play",font="comisansms 10",command=s_11)
            b_12 = Button(root,text="Play",font="comisansms 10",command=s_12)
            b_13 = Button(root,text="Play",font="comisansms 10",command=s_13)
            b_14 = Button(root,text="Play",font="comisansms 10",command=s_14)
            b_15 = Button(root,text="Play",font="comisansms 10",command=s_15)
            b_16 = Button(root,text="Play",font="comisansms 10",command=s_16)
            b_17 = Button(root,text="Play",font="comisansms 10",command=s_17)
            b_18 = Button(root,text="Play",font="comisansms 10",command=s_18)
            b_19 = Button(root,text="Play",font="comisansms 10",command=s_19)
            b_20 = Button(root,text="Play",font="comisansms 10",command=s_20)



            b_p_1 = Button(root,text="Pause ",bg="medium violet red",font="comisansms 15 bold",command=pause)

            b_r_1 = Button(root,text="Resume",bg="medium violet red",font="comicsansms 15 bold",command=resume)

            b_s_1 = Button(root,text="Exit  ",bg="medium violet red",font="comicsansms 15 bold",command=quit_1)




            menubar = Menu(root)
            submenu = Menu(menubar, tearoff=0)
            submenu.add_command(label="Exit",font="comicsansms 9",command=quit)
            menubar.add_cascade(label="File",menu=submenu)
            root.config(menu=menubar)

            song_1.grid(row=2,column=2,pady=10)
            song_2.grid(row=3,column=2,pady=10)
            song_3.grid(row=4,column=2,pady=10)
            song_4.grid(row=5,column=2,pady=10)
            song_5.grid(row=6,column=2,pady=10)
            song_6.grid(row=7,column=2,pady=10)
            song_7.grid(row=2,column=5,pady=10)
            song_8.grid(row=3,column=5,pady=10)
            song_9.grid(row=4,column=5,pady=10)
            song_10.grid(row=5,column=5,pady=10)
            song_11.grid(row=6,column=5,pady=10)
            song_12.grid(row=7,column=5,pady=10)
            song_13.grid(row=2,column=8,pady=10)
            song_14.grid(row=3,column=8,pady=10)
            song_15.grid(row=4,column=8,pady=10)
            song_16.grid(row=5,column=8,pady=10)
            song_17.grid(row=6,column=8,pady=10)
            song_18.grid(row=7,column=8,pady=10)
            song_19.grid(row=8 , column=2,pady=10)
            song_20.grid(row=8 , column=5,pady=10)

            b_1.grid(row=2,column=4,padx=30)
            b_2.grid(row=3,column=4,padx=30)
            b_3.grid(row=4,column=4,padx=30)
            b_4.grid(row=5,column=4,padx=30)
            b_5.grid(row=6,column=4,padx=30)
            b_6.grid(row=7,column=4,padx=30)
            b_7.grid(row=2,column=6,padx=30)
            b_8.grid(row=3,column=6,padx=30)
            b_9.grid(row=4,column=6,padx=30)
            b_10.grid(row=5,column=6,padx=30)
            b_11.grid(row=6,column=6,padx=30)
            b_12.grid(row=7,column=6,padx=30)
            b_13.grid(row=2,column=9,padx=30)
            b_14.grid(row=3,column=9,padx=30)
            b_15.grid(row=4,column=9,padx=30)
            b_16.grid(row=5,column=9,padx=30)
            b_17.grid(row=6,column=9,padx=30)
            b_18.grid(row=7,column=9,padx=30)
            b_19.grid(row=8,column=4,padx=30)
            b_20.grid(row=8,column=6,padx=30)


            b_p_1.grid(row=11 , column=3,padx=20)

            b_r_1.grid(row=11,column=4,pady=30,padx=20)

            b_s_1.grid(row=11,column=5)

            root.mainloop()

        music_play()

    elif aa=="3" :
        ai("Enter for how many minutes you want to set alarm ")
        time_input  = float(input())
        time_input_sec = time_input*60
        ai(f"Your alarm is set for {time_input} minutes , which is {time_input_sec} seconds")
        time.sleep(time_input_sec)
        while(True):
            mixer.init()
            mixer.music.load("alarm.mp3")
            ai("To stop alarm press any key")
            print("To stop alarm press any key")
            mixer.music.play()
            stop = input()
            mixer.music.pause()
            break

    elif aa=="4" :
        ai("Enter which site do yo want to open")
        ac = input()
        site = webdriver.Chrome()
        site.maximize_window()
        site.get(ac)
        ai("Site opened")


    elif aa=="5" :
        ai("Enter song link from youtube \n")
        ad  = input()
        site = webdriver.Chrome()
        site.maximize_window()
        site.get("https://ytmp3.cc/en13/")
        ai("Opening site")
        b = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]")
        b.send_keys(ad)
        convert_button = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[2]")
        convert_button.click()
        time.sleep(4)
        download_buutton = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")
        download_buutton.click()



    elif aa=='6' :
        ai(f"The date is {date.today()}" )

    elif aa=="7":
        ai("This is Rock paper scisor game")
        ai("Starting the game")
        i = 0
        z = 0  # z is  number of time you win
        y = 0
        while i < 10:
            i = i + 1
            print("Total tries left =", 10 - i)
            import random

            print("The number of time you win =", z)
            print("The number of times computer win =", y)
            print(" ")
            # print("The number of time you win ", z)
            list1 = ["1", "2", "3"]
            a = random.randint(1, 3)
            # print(a)
            # input()
            print("Press 1 for rock \n"
                  "Press 2 for paper \n"
                  "Press 3 for siscor \n")
            b = int(input())
            if b == 1:
                print("Your choice is Rock \n")
                if a == 1:
                    print("Computer's choice is Rock ")
                    print("Both are same \n")
                    continue
                elif a == 2:
                    y = y + 1
                    print("Computer's choice is Paper ")
                    print("You lose \n")
                    ai("You lose")
                    continue
                elif a == 3:
                    z = z + 1
                    print("Computer's choice is Sicsor ")
                    print("You win \n")
                    ai("You win")
                    continue

            elif b == 2:
                print("Your choice is paper \n")
                if a == 1:
                    z = z + 1
                    print("Computer's choice is Rock")
                    print("You win \n")
                    ai("You win")
                    continue
                elif a == 2:
                    print("Computer's choice is Paper")
                    print("Both are same \n")
                    continue
                elif a == 3:
                    y = y + 1
                    print("Computer's choice is Sicsor")
                    print("You lose \n")
                    continue
            elif b == 3:
                print("You choice is scisor \n")
                if a == 1:
                    y = y + 1
                    print("Computer's choice is Rock")
                    print("You lose \n")
                    continue
                elif a == 2:
                    z = z + 1
                    print("Computer's choice is Paper")
                    print("You win \n")
                elif a == 3:
                    print("Computer's choice is Scisor")
                    print("Both are same \n")
                    continue
            else:
                print("You entered a wrong choice or EROR \n")

        print("The number of times you won ", z)
        print("The number of times computer won", y)

        if z > y:
            ai("Boss , I am glad you won the game")
            print('Game Over \n'
                  'You won \n')
        elif y > z:
            ai("Boss you lose , no worries , you can always try again")
            print('Game Over \n'
                  'You lose \n')
        elif y == z:
            ai("Boss it's a tie between you and computer")
            print('Game Over \n'
                  'Tie between you and computer \n')

        else:
            print("  \n"
                  "  \n")

        print("Do you want to play again or not \n"
              "Press 1 for playing \n"
              "Press 2 to  exit")

        aaz = int(input())

        if aaz==1:
            print("ok")
            continue

        else :
            print("Ok exiting")
            break

    elif aa=="8" :
        print("Enter file name")

        a = str(input())

        print('Enter file format without "." ')
        b = str(input())
        open(f"{a}.{b}", "w")
        pass

    elif aa=="9":
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
            root.title(f"Made By Shivam ")
            root.geometry("800x600")
            def update():
                text = Text(bg="white", font=f"{style} {size} {bold}")
                text.update()
            def copy():
                a = text.get("1.0", "end")
                py.copy(a)
            def quit_1():
                quit()
            def paste():
                text.insert(END, f"\n{py.paste()}")
            def save_2():
                global var_1, ab
                # var_1 = StringVar()
                Entry(root, textvariable=var_1).grid()
                Button(root, text="Save", command=save).grid()
            def save():
                # var_1 = StringVar()
                global var_1, ab
                # ab = var_1.get()
                ab = var_1.get()
                print(ab)
                a = text.get("1.0", "end")
                with open(f"{ab}.txt", "w") as f:
                    f.write(a)
                tm.showinfo("Save", f"Notepad saved as {ab}.txt ")
            def warning():
                tm.showerror("Warning", "You are not allowed to acess source code, Contact Shivam for further help")
            def support():
                tm.showinfo("Help and Support", "Please contact Shivam \n"
                                                "Mobile no. = 9644971120  \n"
                                                "Email = dhamejanishivam@gmail.com")
            def copy_c_d():
                py.copy("9644971120 , dhamejanishivam@gmail.com")
                tm.showinfo("Work done", "Contact details are copied")
            # Menu -
            main_m = Menu(root)
            m1 = Menu(main_m, tearoff=0)
            m1.add_command(label="Exit", command=quit_1)
            m1.add_command(label="Copy", command=copy)
            m1.add_command(label="Paste", command=paste)
            m1.add_command(label="Save", command=save_2)
            root.config(menu=main_m)
            m2 = Menu(main_m, tearoff=0)
            m2.add_command(label="View Code", command=warning)
            m3 = Menu(main_m, tearoff=0)
            m3.add_command(label="Get Support", command=support)
            m3.add_command(label="Copy contact details", command=copy_c_d)
            m4 = Menu(main_m, tearoff=0)
            m4.add_command(label="Edit font")
            m4.add_command(label="Update", command=update)
            main_m.add_cascade(label="File", menu=m1)
            main_m.add_cascade(label="View", menu=m2)
            main_m.add_cascade(label="Help and Support", menu=m3)
            # main_m.add_cascade(label="Font",menu=m4)
            # Ends Here

            # Text code -
            text = Text(bg="white", font=f"{style} {size} {bold}")
            text.grid(row=0, column=0, columnspan=4, sticky=N + S + E + W)
            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)
            root.mainloop()
            # Ends Here
        if __name__ == "__main__":
            ai("Opening notepad")
            notepad_main()
    elif aa=="10" :
        ai("Enter what you want to serch on google ")
        serch_input = input()
        site = webdriver.Chrome()
        site.maximize_window()
        site.get("https://www.google.com")
        serch_get = site.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input")   
        serch_get.send_keys(serch_input)
        pg.typewrite(["enter"])
        ai("Task completed")
    
    elif aa=="11":
        ai("Opening Calculator")        
        ans = 0
        root = Tk()
        root.title("Made by Shivam")
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

    elif aa=="s" or aa=="S":
        ai(f' Shutting down the laptop')
        os.system("shutdown /s /t 1") 

    elif aa=="Q" or aa=="q" :
        ai("Ok quitting the program")
        sys.exit()
