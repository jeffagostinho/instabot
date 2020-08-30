import time
import random
from datetime import date
from config import config
from helpers import type_like_a_person
from src.repositories.FollowerRepository import FollowerRepository
from src.repositories.CommentControlRepository import CommentControlRepository

class Comment:

    POST_URL = 'https://www.instagram.com/p/'

    def __init__(self, driver, postId):
        self.driver = driver
        self.postId = postId
        self.followerRepository = FollowerRepository()
        self.commentControlRepository = CommentControlRepository()

    def execute(self):
        driver = self.driver

        while (True):
            driver.get(self.POST_URL + str(self.postId))

            try:
                for i in range(40):
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

                    self.saveCommentControl(self.postId)
                    
                    time.sleep(90)

            except Exception as e:
                print(e)
                time.sleep(120)
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]"
                ).click()

            time.sleep(120)
    
    def saveCommentControl(self, postId):
        today = date.today().strftime("%d/%m/%Y")

        self.commentControlRepository.save({
            "post_id": postId,
            "commented_at": today
        },True)
