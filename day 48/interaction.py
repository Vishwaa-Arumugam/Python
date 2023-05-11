from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


chrome_driver_path = "chrome_driver_path"

driver = webdriver.Chrome()

driver.get("corresponding_url_page_address")

search = driver.find_element(By.NAME, "username")
search.send_keys("Python")

pas = driver.find_element(By.NAME, "password")
pas.send_keys("hhh")

b = driver.find_element(By.XPATH, "/html/body/form/input[3]")
b.click()

sleep(3)
driver.quit()
