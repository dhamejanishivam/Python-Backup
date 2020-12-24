import pyautogui as pg
import time



print("Are you ready \n")
print("Do you want to use same number \n"
"Press 1 for yes and 2 for no")
y_n_o = int(input())

if y_n_o==1 :
    a = "+91 9644971120"
else :
    print("Enter your reciver name \n")
    a = input()


print(f'How many do you want to send to {a} \n')
b = int(input())

# Google chrome click - 
pg.doubleClick(x=20, y=532)

time.sleep(4.5)


# Web whatsapp click -
pg.click(x=268, y=87)

time.sleep(13)

# Contack find - 
pg.doubleClick(x=156, y=187)
# Contact click - 
pg.typewrite(a)
pg.typewrite(['enter'])

time.sleep(3)

print("Scroll down and press an key \n")
key = input()
time.sleep(1.3)

c = 1

for i in range(b):
    pg.click(x=676, y=712)
    pg.typewrite(f' {c} , {b-c} ')
    pg.typewrite(['enter'])
    c+=1

print("done")


