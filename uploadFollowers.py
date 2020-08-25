import sys
from src.Driver import Driver
from src.Login import Login
from src.UploadFollowers import UploadFollowers

username = sys.argv[1]
password = sys.argv[2]
user = sys.argv[3]

web = Driver()
driver = web.get()

login = Login(driver, username, password)
login.enter()

uploadFollowers = UploadFollowers(driver, 2000)
uploadFollowers.upload(user)