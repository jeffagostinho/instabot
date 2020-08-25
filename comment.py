import sys
from src.Driver import Driver
from src.Login import Login
from src.Comment import Comment

username = sys.argv[1]
password = sys.argv[2]

web = Driver()
driver = web.get()

login = Login(driver, username, password)
login.enter()

comment = Comment(driver)
comment.send()