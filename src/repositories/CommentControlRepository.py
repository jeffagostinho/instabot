from pymongo import MongoClient
from config import database
from datetime import date

class CommentControlRepository:

    def __init__(self):
        self.commentControl = MongoClient(database['client']).instabot.comment_control

    def save(self, data, upsert=False):
        self.commentControl.update_one(
            data, 
            {
                '$set': data,
                '$inc': {
                    'comments': 1
                }
            }, 
            upsert
        )