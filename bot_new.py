import pyautogui as pg
from PIL import Image , ImageGrab
import time
from numpy import asarray
import win32api
from pynput.keyboard import Controller,Key



name = "KPS"

def testing_2():
    time.sleep(1)
    color = 0
    while color<256 :
        image = ImageGrab.grab().convert("L")
        data = image.load()
        x1 = 512#413
        x2 = 513    #420 # 1158
        y1 = 415#160
        y2 = 417#180 # 700
        for a in range(x1,x2): # 413,1158
            for b in range(y1,y2): # 160,685
                data[a,b] = 102
                color = 256

                # if data[a,b] == color:  #(106,162,188)
                #     print(color)
                # else:
                #     if color<256 :
                #         color+=1
                #         continue
                #     elif color>= 256:
                #         print("Fail")
                #         break
                
    image.show()

# testing_2()

def testing():
    time.sleep(1)
    image = ImageGrab.grab()
    data = image.load()
    x1 = 511#413
    x2 = 512    #420 # 1158
    y1 = 415#160
    y2 = 416#180 # 700
    r = 0
    b = 0
    c = 0
    for a in range(x1,x2): # 413,1158
        for b in range(y1,y2): # 160,685
            
            if data[a,b] >= (106,150,188):
                print("Jugad chal gaya")

            if data[a,b] == (87,133,157) or data[a,b] == (110,167,197) or data[a,b] == (125,180,210)  or data[a,b] == (88,125,144) or data[a,b]==(115,147,160) or data[a,b] == (121,171,198) : #  data[a,b] >= (106,160,188) :
                print("Yes")    
                     
            else:
                print("no")

# testing()


def screenshot():

    image = ImageGrab.grab().convert("L")
    data = image.load()

    x1 = 260
    x2 = 270
    y1 = 200
    y2 = 210

    for p in range(x1,x2):
        for q in range(y1,y2):
            data[p,q] = 0

    # time.sleep(1)
    # image = ImageGrab.grab().convert("L")
    # data = image.load()

    # x1 = 948
    # x2 = 955
    # y1 = 457
    # y2 = 462

    # for p in range (x1,x2):
    #     for q in range(y1,y2):
    #         data[p,q] = 0

    # color = 0
    # while color<256 :
    #     image = ImageGrab.grab().convert("L")
    #     data = image.load()
    #     for p in range (x1,x2):
    #         for q in range(y1,y2):
    #             if data[p,q] == color :
    #                 print(f'color = {color}')
    #                 break
    #     if color<256:
    #         color+=1KPS
    #     elif color>=256:
    #         print(101)
    #         break
    #         return
    # image.show()
    """
    Whatsapp web testing


    x1 = 511#413
    x2 = 530    #420 # 1158
    y1 = 415#160
    y2 = 419#180 # 700
    for a in range(x1,x2): # 413,1158
        for b in range(y1,y2): # 160,685
            data[a,b] = 100  #(106,162,188)
    # i=1
    # while i<10:
    #     i+=1
    #     image = ImageGrab.grab()
    #     data = image.load()
    #     x1 = 413
    #     x2 = 420 # 1158
    #     y1 = 160
    #     y2 = 180 # 700
    #     for a in range(x1,x2): # 413,1158
    #         for b in range(y1,y2): # 160,685
    #             data[a,b] = (106,162,188)
    #     if x2<1158:
    #         x2+=1
    #     if y2<700:
    #         y2+=1
    #     if x2==1158 and y2==700 :
    #         break
    #     image.show()
    #     image.close()

    """    


#     image.show()

# screenshot()


def scanner():
    time.sleep(3)
    while True :
        image = ImageGrab.grab().convert("L")
        data = image.load()
        for p in range(317,330):
            for q in range(125,137):
                if data[p,q] > 50 :
                    return     
                else:
                    continue
        

def scanner_2():
    time.sleep(1)
    # x1 = 413
    # x2 = 420 # 1158
    # y1 = 160
    # y2 = 180 # 700
    x1 = 690
    x2 = 700 # 1158
    y1 = 690
    y2 = 700 # 700
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()        
        for a in range(x1,x2): # 413,1158
            for b in range(y1,y2): # 160,685                
                if data[a,b] == 102: #>= 100 and data[a,b] <= 104:
                    print("Scan 2 completed sucessfully")
                    return x1,y1
                else:
                    pass
        if x1>(413+10):
            x1-=10
        if y1>(160+10):
            y1-=10
        if x1==413 and y1==160 :
            print("Sorry Unable to find \n")
            break
            return "Fail"
        # if x2<(700-10):
        #     x2+=-10
        # if y2<(700-10):
        #     y2+=10
        # if x2==700 and y2==700 :
        #     print("Sorry Unable to find \n")
        #     break
        #     return "Fail"
        

def scanner_3():
    while True:
        # color = 83
        image = ImageGrab.grab().convert("L")
        data = image.load()  
        x1 = 948
        x2 = 955
        y1 = 457
        y2 = 462
        for p in range(x1,x2):
            for q in range(y1,y2):
                if data[p,q] == 83 :
                    print("Scann 3 completed sucessfully")
                    return 
                else :
                    continue

def scanner_4():
    time.sleep(1)
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        x1 = 95
        x2 = 105
        y1 = 270
        y2 =  280
        for p in range(x1,x2):
            for q in range(y1,y2):
                if data[p,q] >= 200 :
                    return
                else:
                    continue


def scanner_5():
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        x1 = 95
        x2 = 105
        y1 = 270
        y2 =  280
        for p in range(x1,x2):
            for q in range(y1,y2):
                if data[p,q] <= 100 :
                    return
                else:
                    continue


def scanner_6():
    x1 = 260
    x2 = 270
    y1 = 200
    y2 = 210
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        for p in range(x1,x2):
            for q in range(y1,y2):
                if data[p,q] <=50 :
                    return
                else:
                    continue
        



def clicker(x,y):
    pg.click(x =x,y = y)

def special_key(String):
    pg.typewrite([String])

def typer(String):
    pg.typewrite(f"{String}")

def move(x,y):
    pg.moveTo(x=x,y=y)

def hotkey_press(key1,key2):
    pg.hotkey(key1,key2)

def double_click(x,y):
    pg.doubleClick(x=x,y=y)

if __name__ == '__main__':
    
    move(517,767)
    time.sleep(1)
    clicker(1365,760)
    time.sleep(1)
    move(517,767)
    time.sleep(1)
    clicker(560,747)
    time.sleep(1)
    hotkey_press('ctrl','n')
    time.sleep(1)
    clicker(285,85)

    scanner()
    
    time.sleep(2)
    double_click(126,185)
    time.sleep(1)
    pg.typewrite(name)
    time.sleep(0.7)
    special_key("enter")
    time.sleep(2)

    position = scanner_2()
    if position=="Fail":
        pass
    else:
        # print(position)
        clicker(position[0],position[1])

    clicker(772, 192)

    scanner_3()

    time.sleep(1)
    clicker(1246,140)
    time.sleep(2)

    scanner_4()

    time.sleep(1)
    clicker(652,478)
    time.sleep(1)

    scanner_5()

    scanner_3()

    time.sleep(0.5)
    hotkey_press('ctrl','d')
    hotkey_press('ctrl','e')
    clicker(968,457)

    scanner_6()

    time.sleep(1.5)
    clicker(1145,117)
    time.sleep(1.5)
    clicker(1260,190)
    time.sleep(0.5)
    clicker(1110,733)
    typer("GOOD MORNING SIR")
    clicker(1323,725)


