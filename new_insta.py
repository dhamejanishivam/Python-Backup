import pyautogui as pg
import time


#  558 , 47 # enter website

# print(pg.position())

pg.click(558,47)

# pg.hotkey("ctrl","x")
# pg.hotkey("ctrl","c")

pg.typewrite("https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet")
pg.typewrite(["enter"])

time.sleep(3)

pg.click(665,255)
pg.typewrite("shivam__dhamejani")
time.sleep(1)
pg.click(x=610, y=294)
time.sleep(1)
pg.typewrite("Iphone510")
time.sleep(1)
pg.click(x=637, y=347)
time.sleep(5)
pg.doubleClick(x=675, y=488)
# time.sleep(5)

i=0
a = input("Press any key to start")
time.sleep(3)
pg.click(x=513, y=275)
while(True):
    if i<=25:
        pg.typewrite(["down"])
        i+=1
    elif i>24 :
        pg.doubleClick(x=548, y=572)
        # pg.click(x=513, y=275)
        i=0
