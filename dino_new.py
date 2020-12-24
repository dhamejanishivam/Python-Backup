import pyautogui as pg
from PIL import Image , ImageGrab
import time
from numpy import asarray
import win32api
from pynput.keyboard import Controller,Key



# # def hit(key):
# #     pg.typewrite([key])
# def long_press(key):
#     pg.keyDown(key)
#     time.sleep(0.2)
#     pg.keyUp(key)
# def match(data):
#     # lower_1 = False
#     # Lower 1st box -
#     for i in range(200,300):
#         for j in range(440,460) :
#             if data[i,j]<=150 and data[i,j]>=120 :
#                 lower_1 = True
#                 return (1)
#     # Lower 2nd box -
#     # for i in range(250, 290):
#     #     for j in range(440, 460):
#     #         if data[i, j] <= 150 and data[i,j] >=120:
#     #             if lower_1==True:
#     #                 return (3)
#     #             else:pass
#     # Upper box -
#     # for j in range(380,400) :
#     #      for i in range(200,350) :
#     #         if data[i,j]<=150 and data[i,j]>=120 :
#     #             return (2)
# long_press("up")
# while(True):
#     image = ImageGrab.grab().convert("L")
#     data = image.load()
#     match(data)
#     if match(data) == 1 :
#         long_press("up")
#         continue
#     # if match(data) == 2 :
#     #     hit("down")
#     #     continue
#     # if match(data) == 3 :
#     #     long_press("up")
#     #     continue


def screenshot():
    time.sleep(1)
    image = ImageGrab.grab().convert("L")
    data = image.load()
    for i in range(200,240):
        for j in range(440,460) :
            data[i, j] = 120
    for j in range(380,400) :
        for i in range(200,350) :
            data[i ,j ] = 150
    image.show()

screenshot()
