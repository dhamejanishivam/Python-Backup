from pygame import mixer
from tkinter import *
import os

def music_play():
    root = Tk()
    root.geometry("1000x500")
    # root.maxsize(700,500)
    # root.minsize(700,500)
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
        mixer.music.load("bella.mp3")
        mixer.music.play()

    root.title('Made by Shhivam')
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
    song_20 = Label(root,text="Bella Cioa",bg="blue",fg="yellow",font="comicsansms 12")


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
    b_20 = Button(root,text='Play',font='comicsansms 10',command=s_20)


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
    song_20.grid(row=8,column=5,pady=10)

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

if __name__ == "__main__":
    music_play()