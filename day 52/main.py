from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from time import sleep

INSTA_USER_NAME = "user_name"
INSTA_PASSWORD = "password"


class Insta_follower:

    # if using xpath as an identifier kindly copy the full xpath from browser    
    
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(5)

        self.driver.maximize_window()

        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(INSTA_USER_NAME)

        sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(INSTA_PASSWORD)

        sleep(5)

        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()

        sleep(10)

    def find_follower(self):

        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        sleep(2)
        self.driver.get(f"https://www.instagram.com/chefsteps/followers")
        sleep(5)

    def follow(self):

        self.driver.find_element(By.XPATH,
                                 '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div/div/div/div[3]/div/button/div/div').click()
        sleep(5)




insta_assignment = Insta_follower()
insta_assignment.login()
insta_assignment.find_follower()
insta_assignment.follow()
