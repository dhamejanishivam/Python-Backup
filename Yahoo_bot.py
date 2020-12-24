from  selenium import webdriver
import time
import pyperclip as pc
import tkinter as tk
import  random
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
r_new = random.choice(UPCASE_CHARACTERS)
pass1 = random.choice(new_list)
r_digit1 = random.choice(DIGITS)
r_low1 = random.choice(LOCASE_CHARACTERS)
r_up1 = random.choice(UPCASE_CHARACTERS)


z = r_new + r_digit + r_low + r_up + pass1 + r_digit1 + r_low1 + r_up1


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

c = f"{name1}_{r_digit}_{r_digit1}_{name2}"

#  Username genrator code ends here.


# Mobile number genrator -
digit = ["8" , "9"]

mn1 = random.choice(digit)
mn2 = random.choice(DIGITS)
mn3 = random.choice(DIGITS)
mn4 = random.choice(DIGITS)
mn5 = random.choice(DIGITS)
mn6 = random.choice(DIGITS)
mn7 = random.choice(DIGITS)
mn8 = random.choice(DIGITS)
mn9 = random.choice(DIGITS)
mn10 = random.choice(DIGITS)

final_mn = mn1+mn2+mn3+mn4+mn5+mn6+mn7+mn8+mn9+mn10
mn = int(final_mn)
# print(mn)

# Mobile number gerator ends here.

# Birth month genrator -

birth_moth_list = ["January" , "February" , "March" , "September"]

bml = random.choice(birth_moth_list)

# Birth month genrator code ends here.

# Birth day genrator -

bdl = random.choice(DIGITS)

# Birth day genrator code ends here.






# site = webdriver.Chrome() # Donot use this code while using private tab because it will open 2 tab

# Incognito mode code starts here =

private = webdriver.ChromeOptions()
private.add_argument('--incognito')
site = webdriver.Chrome(chrome_options=private)

# Incognito mode code ends here

site.maximize_window()
site.get("https://login.yahoo.com/account/create?specId=yidReg")

time.sleep(3)



first_name = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/fieldset/div/div[1]/input")
first_name.send_keys(name1)


last_name = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/fieldset/div/div[2]/input")
last_name.send_keys(name2)


password_input = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/div[2]/input[1]")
password_input.send_keys(z)


email_input = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/div[1]/div[1]/input")
email_input.send_keys(c)


mobileno_input = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/div[3]/div[3]/input")
mobileno_input.send_keys(mn)

birth_month_input = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/div[4]/div[1]/select")
birth_month_input.send_keys(bml)
birth_month_input.click()


birth_day_input = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/div[4]/div[2]/input")
birth_day_input.send_keys(bdl)
birth_day_input.click()


birth_year_input = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/div[4]/div[3]/input")
birth_year_input.send_keys("1999")
birth_year_input.click()



continue_button = site.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div/form/div[8]/button")
continue_button.click()



print(f"Your name is  {name1} {name2} ")
print("\n")
print(f"Your email id is {c}")
print("\n")
print(f"Your mobile number is {mn}")
print("\n")
print(f"Your password is {z} ")