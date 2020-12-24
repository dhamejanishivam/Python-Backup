from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

print("Enter the name of reciver same as in your whatsapp")



print("Use my number \n"
      "Press 1 for yes \n"
      "2 for no \n")

c = int(input())

if c==1:
    b= "+91 9644971120"
else:
    print("My number is \n"
          "+91 9644971120")

    b = input()
print("Enter the amount of message you want to send")

c = int(input())
if c==0:
    raise Exception ("0 is not allowed")
else:
    pass
site = webdriver.Chrome()
site.maximize_window()
site.get("https://web.whatsapp.com/")

print("Please scan qr and let the site load and then press any key")

a = input()

# Serch box code -

serch_box = site.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
serch_box.click()
serch_box.send_keys(b)
serch_box.send_keys(Keys.ENTER)

# Serch box code ends here.

# Not working method -

# new_chat_button = site.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div/span")
# # /html/body/div[1]/div/div/div[3]/div/header/div[2]/div/span/div[2]/div/span
# new_chat_button.click()
#
# serch_contact_box = site.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/span/div/span/div/div[1]/div/label/div/div[2]")
# serch_contact_box.click()
# serch_contact_box.send_keys(b)
# serch_contact_box.send_keys(Keys.ENTER)

# Ends here




i = 0

while(i<=c):
    message_box = site.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
    message_box.click()

    message_box.send_keys(f" Sorry mummy , Ye {i} message hai , abhi aur {c - i} baki hai")

    send_button = site.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button")
    send_button.click()

    i+=1


print("Everything worked perfectly")