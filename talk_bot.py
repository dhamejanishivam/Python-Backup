from win32com.client import Dispatch
from datetime import datetime
from datetime import date
# from pygame import mixer
import time
# from tkinter import *
# import os
# from selenium import webdriver
# import pyautogui as pg
# import sys



def ai(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


ai('Enter what you want to talk')


wish = [ "Hello" ,"hello","good morning"]
wish_reply = ["Hi","hi","good morning"]



while True :

    a = input()
    
    for item in wish:
        if a==item:
            b = wish.index(item)
            ai(wish_reply[b])
            break
    else:
        ai("I am not sure I understand")

