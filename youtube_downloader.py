import time
from selenium import webdriver


print("Insert video link from yutube \n")

a = input()

site = webdriver.Chrome()

print("Do yo want to download it in mp3 or video \n"
      "Press 1 for video download \n"
      "Press 2 for mp3 download \n"
      "")

b = int(input())



if b==1 :
    d = int(input())
    site.get("https://en.savefrom.net/1-youtube-video-downloader-4/")
    time.sleep(2)
    c = site.find_element_by_xpath("/html/body/div/div[1]/div[1]/div/div[1]/div[2]/div/form/div[1]/div/input")
    c.send_keys(a)
    # next_button = site.find_element_by_xpath("/html/body/section[1]/div/div[1]/div/div/div/form/div/div[2]/button")
    # next_button.click()
    download_button = site.find_element_by_xpath("/html/body/div/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[2]/div[1]/a")
    download_button.click()

