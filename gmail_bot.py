from selenium import webdriver
import time

a = webdriver.Chrome()

private = webdriver.ChromeOptions()
private.add_argument("--incognito")
a = webdriver.Chrome(chrome_options=private)

time.sleep(3)

a.maximize_window()

a.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

time.sleep(2)

username_input = a.find_element_by_name("identifier")
username_input.send_keys("dhamejanishivam")
next1 = a.find_element_by_class_name("VfPpkd-RLmnJb")
next1.click()
time.sleep(3)
password_input = a.find_element_by_name("password")
password_input.send_keys("Iloveyou_3000")
next2 = a.find_element_by_class_name("VfPpkd-RLmnJb")
next2.click()

