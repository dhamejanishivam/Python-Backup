from selenium import  webdriver
import time
print("All input should be in small \n")

while(True):

    print("What do you want to open \n"
          "c for code with harry python \n"
          "b for bb ki vines \n"
          "a for ashish chancalani \n"
          "m for mostly sane \n"
          "Or you can input what you want to open \n")
    a = input()

    if a=="c" :
        site = webdriver.Chrome()
        site.maximize_window()
        site.get("https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME")

    elif a=="b":
        site = webdriver.Chrome()
        site.maximize_window()
        site.get("https://www.youtube.com/results?search_query=bb+ki+vines")

    elif a=="a" :
        site = webdriver.Chrome()
        site.maximize_window()
        site.get("https://www.youtube.com/results?search_query=ashish+chanchlani")

    elif a=="m" :
        site = webdriver.Chrome()
        site.maximize_window()
        site.get("https://www.youtube.com/results?search_query=mostlysane")

    else :
        site = webdriver.Chrome()
        site.maximize_window()
        site.get("https://www.youtube.com/")
        time.sleep(1)

        serch = site.find_element_by_xpath(
            "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input")
        serch.send_keys(a)

        serch_button = site.find_element_by_xpath("//*[@id='search-icon-legacy']")
        serch_button.click()



