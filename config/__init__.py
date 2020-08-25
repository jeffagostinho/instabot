import json

with open('config/config.json', 'r') as f:
    config = json.load(f)

with open('config/database.json', 'r') as f:
    database = json.load(f)