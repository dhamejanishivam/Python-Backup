import pyautogui as pg
from PIL import Image , ImageGrab
import time
from numpy import asarray


    pg.keyDown(key)
def hit(key):

def isCollide(data):
    for i in range(270,340):
            for j in range(400,500):
                if data[i , j] < 100 :
                    return True
    return False                



if __name__ == "__main__":
    time.sleep(3)
    hit("up")
    for i in range(270,340):
            for j in range(400,500):
                if data[i , j] < 100 :
    while(True):
        image = ImageGrab.grab().convert("L")   
        data = image.load()
        if isCollide(data):
            hit("up")
