from selenium import webdriver
import pyautogui
import sys
import time
import datetime

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")


driver.get('https://www.sgsstudentbostader.se/')
driver.find_element_by_class_name('mina-sidor-button').click()
driver.find_element_by_class_name('mypages-image').click()

time.sleep(10)
pyautogui.click(x=137, y=487)
pyautogui.typewrite(sys.argv[1])
pyautogui.click(x=137, y=553)
pyautogui.typewrite(sys.argv[2])
time.sleep(1)

driver.find_element_by_class_name('sgs-link-to').click()

time.sleep(10)
driver.save_screenshot('updated_latest.png')

print(str(sys.argv[0]) + 'finished at ' + str(datetime.datetime.now()))

driver.close()
