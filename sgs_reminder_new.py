from selenium import webdriver
import pyautogui



driver = webdriver.Chrome()

driver.get('https://www.sgsstudentbostader.se/')
driver.find_element_by_class_name('mina-sidor-button').click()
driver.find_element_by_class_name('mypages-image').click()