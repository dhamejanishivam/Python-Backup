from selenium import webdriver
import time
import pyperclip as pc
import tkinter as tk
import random
import array




print("Do you want to sign in from temprory email \n"
      "Press 1 for yes \n"
      "Press 2 for no \n")
q = int(input())

print("Ok")

print("\n"
      "Which website you want to use for temprory mail \n"
      "1 for Temp mai \n"
      "2 for Temprory mail \n"
      "3 for Fake mail \n")

aq = int(input())

if q==1 :
    if aq==1 :
        site1 = webdriver.Chrome()
        site1.get("https://tempail.com/en/")
        time.sleep(2)
        copy = site1.find_element_by_xpath("/html/body/section[1]/div[2]/div/div[4]/a[1]")
        copy.click()
        root = tk.Tk()
        root.withdraw()
        a = root.clipboard_get()
        print(a)

    elif aq==2 :
        site2 = webdriver.Chrome()
        site2.get("https://temp-mail.org/en/")
        time.sleep(2)
        copy2 = site2.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/form/div[2]/button")
        copy2.click()
        root = tk.Tk()
        root.withdraw()
        a = root.clipboard_get()
        print(a)

    elif aq==3 :
        site3 = webdriver.Chrome()
        site3.get("https://www.fakemail.net/")
        time.sleep(2)
        copy3 = site3.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div")
        copy3.click()
        root = tk.Tk()
        root.withdraw()
        a = root.clipboard_get()
        print(a)

    else :
        print(" \n"
              "Wrong input \n")


else:
    print("Enter an fake email \n"
          "You can find fake email at temp mail or etc \n"
          "\n")
    a = input()







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




# print("Enter name to create a account with \n"
#       "\n")
# b = input()


# print("Enter account username \n"
#       "It must be unique \n"
#       "And if username not availabel so re run programm \n"
#       "\n")
#
# c = input()

# print("Enter account password \n"
#       "It must be unique \n"
#      "\n")
#
# y = input()


site = webdriver.Chrome()
#
# print("Disable all cookies \n"
#       "And press any key after diasabling cookies \n"
#       "\n")
# i = input()

# Incognito mode code starts here =

# private = webdriver.ChromeOptions()
# private.add_argument('--incognito')
# site = webdriver.Chrome(chrome_options=private)

# Incognito mode code ends here


site.maximize_window()
site.get("https://www.instagram.com/")

time.sleep(3)

sing_up = site.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[2]/div/p/a/span")
sing_up.click()
time.sleep(2)

email_input = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
email_input.send_keys(str(a))

name_input = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input")
name_input.send_keys(b)


username_input = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input")
username_input.send_keys(c)


password_input = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input")
password_input.send_keys(z)


sing_up_button = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div")
sing_up_button.click()

time.sleep(3)

birth_month = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select")
birth_month.send_keys("May")
birth_month.click()

birth_date = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select")
birth_date.send_keys(23)
birth_date.click()

birth_year = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select")
birth_year.send_keys("1999")
birth_year.click()

next_button = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[6]")
next_button.click()

time.sleep(3)

# otp_email1 = site1.find_element_by_xpath("/html/body/section[2]/div/div/div/ul/li[2]/a/div[3]")
# op = otp_email1.text


print("Enter conformation code sent by email Here - \n"
      "")

o = input()

otp_email = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input")
otp_email.send_keys(o)

next_button1 = site.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]")
next_button1.click()



print("Your email is = ", a)
print(" \n")
print("Your username is = " , c)
print("\n")
print("Your password is = " , z)
print("\n")
print("Your name is = " , b )
