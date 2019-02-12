from selenium import webdriver
import sys
import time
import datetime
#from pyvirtualdisplay import Display

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('start-maximized')
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

driver.get('https://www.sgsstudentbostader.se/Mina-sidor/Login?return=https://www.sgsstudentbostader.se/sv-se/mina-sidor')
driver.find_element_by_name('User').send_keys(sys.argv[1])
driver.find_element_by_name('Password').send_keys(sys.argv[2])

driver.find_element_by_class_name('btn-primary').click()

time.sleep(10)

driver.execute_script("window.scrollTo(0, 800)")
driver.save_screenshot('updated_latest.png')
print(str(sys.argv[0]) + 'finished at ' + str(datetime.datetime.now()))

driver.close()
