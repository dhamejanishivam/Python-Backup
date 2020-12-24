from selenium import webdriver
import time
site = webdriver.Chrome()
site.maximize_window()
site.get("https://dopagent.indiapost.gov.in/corp/AuthenticationController?FORMSGROUP_ID__=AuthenticationFG&__START_TRAN_FLAG__=Y&__FG_BUTTONS__=LOAD&ACTION.LOAD=Y&AuthenticationFG.LOGIN_FLAG=3&BANK_ID=DOP&AGENT_FLAG=Y")
time.sleep(2)


agent_id_input = site.find_element_by_xpath("/html/body/form/div/div[2]/div/div/div/div[3]/div[3]/p[3]/span[2]/span/input")
agent_id_input.send_keys("DOP.MI4938810100002")

password_input = site.find_element_by_xpath("/html/body/form/div/div[2]/div/div/div/div[3]/div[3]/p[4]/span[2]/input")
password_input.send_keys("mdtd@2109")

log_in_button = site.find_element_by_xpath("/html/body/form/div/div[2]/div/div/div/div[3]/div[3]/p[8]/span/input[1]")
log_in_button.click()

time.sleep(4)

account_button = site.find_element_by_xpath("/html/body/form/div[1]/div[2]/p/span[8]/a")
account_button.click()
time.sleep(4)

agent_update_button = site.find_element_by_xpath("/html/body/form/div[1]/div[3]/div/span/a[1]")
agent_update_button.click()
time.sleep(4)
