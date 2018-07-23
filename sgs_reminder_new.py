from selenium import webdriver
import pyautogui
import sys
import time
import os
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800,800))
display.start()

#os.environ['DISPLAY'] = '0.0'
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

driver.close()
