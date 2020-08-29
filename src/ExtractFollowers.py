import time
from datetime import datetime
from src.repositories.FollowerRepository import FollowerRepository
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ExtractFollowers:
    INSTA_URL = 'https://www.instagram.com/'

    def __init__(self, driver, userProfile, maxFollowers):
        self.driver = driver
        self.userProfile = userProfile
        self.maxFollowers = int(maxFollowers)
        self.followerRepository = FollowerRepository()

    def getUsernamesFollowers(self):
        self.driver.get(self.INSTA_URL + self.userProfile)
        followersLink = self.driver.find_element_by_css_selector('ul li a')
        followersLink.click()
        time.sleep(2)
        followersList = self.driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
        numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

        followersList.click()
        actionChain = webdriver.ActionChains(self.driver)
        while (numberOfFollowersInList < self.maxFollowers):
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
            print(numberOfFollowersInList)
        
        followersLinks = []
        for user in followersList.find_elements_by_css_selector('li'):
            userLink = user.find_element_by_css_selector('a').get_attribute('href')
            print(userLink)
            followersLinks.append(userLink)
            if (len(followersLinks) == self.maxFollowers):
                break

        usernames = []
        for followerLink in followersLinks:
            usernames.append(followerLink.replace(self.INSTA_URL, '').replace('/', ''))

        return usernames

    def execute(self):
        usernames = self.getUsernamesFollowers()

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
