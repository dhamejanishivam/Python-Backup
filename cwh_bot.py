import pyautogui as pg 
import random
import time
from username_and_other import signup_info


def clicker(x,y):
    pg.click(x=x,y=y)

def typer(string):
    pg.typewrite(string)

def hotkeys(a,b):
    


if __name__ == "__main__":

    clicker(1280,137)
    clicker(518,263)
    typer(signup_info()[2])
    clicker(493,332)
    typer(signup_info()[0])
    clicker(545,413)
    typer(signup_info()[1])
    clicker(267,10)
    clicker(252,52)
    typer("https://www.fakemail.net/")
    time.sleep(6)
    clicker(217,288)
    time.sleep(5)
    clicker(745,238)
    clicker()

