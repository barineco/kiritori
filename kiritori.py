import os
from atproto import Client

username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')

api = Client()
api.login(username, password)

api.send_post('✄------------ test ------------✄')