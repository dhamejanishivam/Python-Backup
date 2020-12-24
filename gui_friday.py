from tkinter import *
from win32com.client import Dispatch
from datetime import datetime
import time



def ai(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

now = datetime.now()
hour = now.strftime("%H")
minute = now.strftime("%M")
realtime = now.strftime("%H:%M:%S")
hour = int(hour)
minute = int(minute)



def time_show():
    if 16<=hour<=23:
        ai('Good Evening boss')
        return 'Good afternoon Boss'
    elif 12<=hour<=15 :
        ai('Good Evening boss')
        return 'Good afternoon Boss'

def fun_start():
    time = time_show()
    


root = Tk()

root.geometry('900x500')
root.title("Friday")
root.configure(bg="white")

text_show = 'Welcome Boss'

t = Text(height=4,width=25,bg="black",fg='white')
t.grid(row=0,column=1)
# root.columnconfigure(0,weight=0)
t.insert(END,text_show)


start = Button(root,text='Start',command=fun_start)
start.grid()

root.mainloop()
