import time
import random
from selenium.webdriver.common.keys import Keys
from config import config
from helpers import type_like_a_person

class Login:

    def __init__(self, driver, username, password):
        self.username = username
        self.password = password
        self.driver = driver

    def execute(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        type_like_a_person(self.username, user_element)
        time.sleep(3)
        
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        type_like_a_person(self.password, password_element)
        time.sleep(3)

        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

        save_info_button = driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]")

        if (save_info_button):
            save_info_button.click()

        time.sleep(3)