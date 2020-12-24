from selenium import webdriver
import time
print("Enter what to serch in youtube")
a = input()
site = webdriver.Chrome()
site.maximize_window()
# time.sleep(2)

site.get("https://www.youtube.com/")
time.sleep(1)

serch = site.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
serch.send_keys(a)


serch_button = site.find_element_by_xpath("//*[@id='search-icon-legacy']")
serch_button.click()




