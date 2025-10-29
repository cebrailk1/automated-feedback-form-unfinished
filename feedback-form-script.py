from asyncio import selector_events
from lib2to3.pgen2 import driver
from optparse import Option
from pydoc import visiblename
from re import T
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from select import select
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
time.sleep(1)

driver.get('https://fox.mynikevisit.com/')
print(driver.title)

time.sleep(1)
driver.find_element("id",'im_policy_accept_button').click()
time.sleep(1)
driver.find_element("id",'option_1114305_412723').click()
time.sleep(1)
driver.find_element("id",'surveyApp_body').click()
time.sleep(1)
driver.find_element("id",'topLevelSelector').click()
time.sleep(4)
print(driver.title)

driver.find_element("xpath",'//*[@id="nextPageLink"]').click()

dropdownbox = driver.find_elements(by=By.TAG_NAME, value="option")
dropdownbox[6].click()

time.sleep(3)

weiter = driver.find_element(By.ID, "nextPageLink")
weiter.click()

time.sleep(3)

driver.find_element(by=By.ID, value= 'promptInput_410092').send_keys('07/04/2023')

time.sleep(3)
dropdownbox = driver.find_elements(by=By.TAG_NAME, value="option")
dropdownbox[3].click()

driver.find_element(by=By.ID, value= 'promptInput_410096').send_keys('109.99')

time.sleep(3)
weiter.click()
driver.find_element("id", 'option_1238704_536896')
time.sleep(3)
weiter.click()

driver.find_element("id", 'option_1238700_536896')
driver.find_element(by=By.ID, value= 'commentArea_536909').send_keys('Schöner Store, gute Lage und sehr viel Sortiment')
time.sleep(3)


driver.find_element("id", 'option_1238342_536620')

driver.find_element("id", 'option_831212_375186')

driver.find_element(by=By.ID, value= 'commentArea_375187').send_keys('Mike hat mich super beraten!')

weiter.click()



time.sleep(5)

driver.quit()