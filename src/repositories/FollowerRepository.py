from pymongo import MongoClient
from config import database

class FollowerRepository:

    def __init__(self):
        self.followers = MongoClient(database['client']).instabot.followers

    def save(self, filter, data, upsert=False):
        self.followers.update_one(
            filter, 
            {
                '$set': data
            }, 
            upsert
        )

    def getAll(self):
        return self.followers.find({})

    def getFollowerUsernameToComment(self):
        follower = self.followers.find_one({}, sort=[('comments_count', 1)])
        follower['comments_count'] += 1

        self.save(
            {
                "username": follower['username'],
            }, 
            follower, 
            True
        )

        return follower['username']