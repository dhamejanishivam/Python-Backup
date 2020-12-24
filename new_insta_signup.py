import pyautogui as pg
import time
from selenium import webdriver
import time
import pyperclip as pc
import tkinter as tk
import random
import array




#  Password genrator code starts here -
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                    'z']
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
'Z']
new_list = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS
r_digit = random.choice(DIGITS)
r_low = random.choice(LOCASE_CHARACTERS)
r_up = random.choice(UPCASE_CHARACTERS)
pass1 = random.choice(new_list)
r_digit1 = random.choice(DIGITS)
r_low1 = random.choice(LOCASE_CHARACTERS)
r_up1 = random.choice(UPCASE_CHARACTERS)
z = r_digit + r_low + r_up + pass1 + r_digit1 + r_low1 + r_up1
#  password genrator code ends here

#  Name genrator -
r_low = random.choice(LOCASE_CHARACTERS)
r_up = random.choice(UPCASE_CHARACTERS)
r_low1 = random.choice(LOCASE_CHARACTERS)
r_up1 = random.choice(UPCASE_CHARACTERS)
r_low2 = random.choice(LOCASE_CHARACTERS)
r_low3 = random.choice(LOCASE_CHARACTERS)
r_low4 = random.choice(LOCASE_CHARACTERS)
r_low5 = random.choice(LOCASE_CHARACTERS)
r_low6 = random.choice(LOCASE_CHARACTERS)
name1 =  r_up + r_low + r_low1 + r_low2
name2 = r_up1 + r_low3 + r_low4 + r_low5 + r_low6
b = f"{name1}_{name2}"
# print(f"{name1}_{name2} ")
#  name genrator ends here

# Username genrator -
c = f"{name1}__{r_digit}_{r_digit1}__{name2}__"
#  Username genrator code ends here.




#  558 , 47 # enter website

# print(pg.position())

pg.click(558,47)

# pg.hotkey("ctrl","x")
# pg.hotkey("ctrl","c")

pg.typewrite("www.fakemail.net/")
pg.typewrite(["enter"])
time.sleep(5)
pg.click(x=762, y=247)
abcd = [pg.hotkey("ctrl","v")]
time.sleep(1)
pg.click(x=273, y=20)
time.sleep(2)
pg.typewrite("https://www.instagram.com/accounts/emailsignup/")
pg.typewrite(["enter"])
time.sleep(3)
pg.click(x=681, y=365)
pg.hotkey("ctrl","v")
pg.click(x=588, y=417)
pg.typewrite(b)
pg.click(x=586, y=457)
pg.typewrite(c)
pg.click(x=641, y=502)
pg.typewrite(z)
time.sleep(1)
pg.click(x=673, y=550)
time.sleep(2)

# Birth -
# pg.click(x=618, y=360)#month
# pg.click(x=618, y=430) #Birth month selector
# pg.click(x=683, y=362)#Birth date
# pg.click(x=683, y=430)#Birth date
pg.click(x=750, y=358)#Birth year
pg.click(x=745, y=680)#Birth year


# Next button
time.sleep(1)
pg.click(x=678, y=465)
time.sleep(4)

# Again conformationa mail
pg.click(x=111, y=7)
time.sleep(2)

pg.click(x=333, y=282)#Refresh mail
time.sleep(3)
# pg.click(x=333, y=282)#Refresh mail
# time.sleep(1)
pg.click(x=333, y=282)#Refresh mail
time.sleep(3)
# pg.click(x=333, y=282)#Refresh mail



# Mail click
pg.click(x=686, y=405)
time.sleep(2)

# Copy mail
pg.click(x=697, y=593)
pg.doubleClick(x=697, y=593)
pg.hotkey("ctrl","c")

# Insta page

pg.click(x=363, y=0)
pg.click(x=638, y=357)
pg.typewrite(pg.hotkey("ctrl","v"))
pg.typewrite(["enter"])


# pg.click(x=680, y=405)#Next button
time.sleep(4)
