from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


print("Enter how many message you want to send \n")
abc = int(input())
browser = webdriver.Chrome()

# Private mode code starts here -

# private = webdriver.ChromeOptions()
# private.add_argument("--incognito")
# browser = webdriver.Chrome(chrome_options=private)

#  Private mode code ends here.

browser.maximize_window()
browser.get("https://www.instagram.com/")

time.sleep(2)

username_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
username_input.send_keys("fake.id7616")

password_input = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
password_input.send_keys("Iloveyou_3000")

login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
login.click()

time.sleep(3)

not_now_button = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
not_now_button.click()

time.sleep(3)

not_now_button_2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
not_now_button_2.click()

time.sleep(2)

direct_button = browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a")
direct_button.click()
# DM class  = xWeGp

time.sleep(3)

mohit_dm = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a")
mohit_dm.click()

i = 0

while(i<=abc):

    message_button = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    message_button.click()
    message_button.send_keys(f"Message sent {i} , Message left {abc-i} ")

    send_button = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button")
    send_button.click()


    i+=1
print("Everything is working")