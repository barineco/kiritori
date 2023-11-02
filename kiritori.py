import os
from atproto import Client
from datetime import datetime, timedelta, timezone
import time

username = os.getenv('BSKY_USERNAME')
password = os.getenv('BSKY_PASSWORD')

api = Client()
api.login(username, password)

JST = timezone(timedelta(hours=+9))
now = datetime.now(JST)
wait_seconds = (60 - now.minute - 1) * 60 + (60 - now.second)
time.sleep(max(wait_seconds, 0))

while datetime.now(JST).minute != 0:
    time.sleep(1)

current_time_jst = datetime.now(JST).strftime("%H:%M")

api.send_post(f'✄------------ {current_time_jst} ------------✄')
