import asyncio
import json
from pyrogram import Client, filters
import re
from rtl import rtl
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton
from time import sleep
import random
import pytz
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

PROXY = {
    "scheme": "http",  # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",
    "port": 8000,
    "username": "",
    "password": ""
}

API_ID = 17987364
API_HASH = "cf9f342410bef3556dcd7ead7c50dab3"

app = Client('my_account', api_id=API_ID, api_hash=API_HASH)

print('bot started')


def main():
    # tz = pytz.timezone('Asia/Tehran')
    # now = datetime.now(tz)
    # current_time = now.strftime('%H:%M')
    # await app.update_profile(last_name=f'[{str(current_time)}]')
    # print(f'lastname changed {current_time}')

    app.send_message(7430246479, '🥚GET')


scheduler = AsyncIOScheduler()
scheduler.add_job(main, 'cron', minute='*/10')
scheduler.start()

app.run()
