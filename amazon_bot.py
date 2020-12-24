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
site.get("https://www.amazon.in/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F_encoding%3DUTF8%26ref_%3Dnav_ya_signin&prevRID=682J3CSCWG22V64S4VAR&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")

time.sleep(3)



name_input = site.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input")
name_input.send_keys(f"{name1}{name2}")



mobile_input = site.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div/div/div/div[2]/input")
mobile_input.send_keys(mn)


pass_input = site.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[4]/div/input")
pass_input.send_keys(z)

continue_button = site.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/form/div/div/div[6]/span/span/input")
continue_button.click()

