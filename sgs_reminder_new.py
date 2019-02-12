from selenium import webdriver
import sys
import time
import datetime
#from pyvirtualdisplay import Display

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('no-sandbox')
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

driver.get('https://www.sgsstudentbostader.se/Mina-sidor/Login?return=https://www.sgsstudentbostader.se/sv-se/mina-sidor')
driver.find_element_by_name('User').send_keys(sys.argv[1])
driver.find_element_by_name('Password').send_keys(sys.argv[2])

driver.find_element_by_class_name('btn-primary').click()

time.sleep(10)

# pyautogui.click(x=137, y=487)
# pyautogui.typewrite(sys.argv[1])
# pyautogui.click(x=137, y=553)
# pyautogui.typewrite(sys.argv[2])
# time.sleep(1)
#
# driver.find_element_by_class_name('sgs-link-to').click()
#
# time.sleep(10)
driver.save_screenshot('updated_latest.png')
#
print(str(sys.argv[0]) + 'finished at ' + str(datetime.datetime.now()))

driver.close()
