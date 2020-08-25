import time
from datetime import datetime
from src.repositories.FollowerRepository import FollowerRepository
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class UploadFollowers:

    def __init__(self, driver, max):
        self.driver = driver
        self.max = max
        self.followerRepository = FollowerRepository()

    def getUsernamesFollowers(self, username):
        self.driver.get('https://www.instagram.com/' + username)
        followersLink = self.driver.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.driver)
        while (numberOfFollowersInList < self.max):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followersLinks = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followersLinks.append(userLink)
            if (len(followersLinks) == self.max):
                break

        usernames = []
        for followerLink in followersLinks:
            usernames.append(followerLink.replace('https://www.instagram.com/', '').replace('/', ''))

        return usernames

    def upload(self, username):
        usernames = self.getUsernamesFollowers(username)

        for username in usernames:

            filter = {
                "username": '@' + str(username)
            }

            follower = {
                "username": '@' + str(username),
                "comments_count": 0,
                "created_at": datetime.now()
            }

            self.followerRepository.save(filter, follower, True)
