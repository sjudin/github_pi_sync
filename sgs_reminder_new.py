from selenium import webdriver


driver = webdriver.Chrome(executable_path='/usr/lib/chromium-browser')

driver.get('https://www.sgsstudentbostader.se/')
driver.find_element_by_class_name('mina-sidor-button').click()
driver.find_element_by_class_name('mypages-image').click()