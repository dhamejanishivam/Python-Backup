from selenium import webdriver
from time import *

print("Enter song link from youtube \n")

a = input()

site = webdriver.Chrome()

site.minimize_window()

site.get("https://ytmp3.cc/en13/")

b = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[1]")
b.send_keys(a)


convert_button = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/form/input[2]")
convert_button.click()

sleep(4)

download_buutton = site.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[3]/a[1]")
download_buutton.click()

