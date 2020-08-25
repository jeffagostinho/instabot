import time
import random
from config import config
from helpers import type_like_a_person
from src.repositories.FollowerRepository import FollowerRepository

class Comment:

    def __init__(self, driver):
        self.driver = driver
        self.followerRepository = FollowerRepository()

    def send(self):
        driver = self.driver

        while (True):
            for post in config['posts']:
                driver.get(post)

                try:
                    for i in range(6):
                        driver.find_element_by_class_name("Ypffh").click()
                        commentInput = driver.find_element_by_class_name("Ypffh")
                        time.sleep(random.randint(2, 5))
                        followerUsername = self.followerRepository.getFollowerUsernameToComment()

                        type_like_a_person(
                            followerUsername,
                            commentInput
                        )

                        time.sleep(random.randint(3, 5))
                        
                        driver.find_element_by_xpath(
                            "//button[contains(text(), 'Publicar')]"
                        ).click()
                        
                        time.sleep(random.randint(3, 5))

                except Exception as e:
                    print(e)
                    time.sleep(120)
                    driver.find_element_by_xpath(
                        "//button[contains(text(), 'Publicar')]"
                    ).click()

                time.sleep(300)
