import os
from atproto import Client
from datetime import datetime, timedelta, timezone

username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')

current_time_jst = datetime.now(timezone(timedelta(hours=+9))).strftime("%H:%M")

api = Client()
api.login(username, password)

api.send_post(f'✄------------ {current_time_jst} ------------✄')
