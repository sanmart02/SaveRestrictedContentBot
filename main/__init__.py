#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 27885485
API_HASH = "7dd9974c713787410beae4a295cc1e2d"
BOT_TOKEN = "6557904620:AAEhekYh5px21WiKYOmtUnTJu03xmKJTAR8"
SESSION = "AQBtgthwr6lSq4LL0YU-JSQ5QUyF2L4ave_AuIfyR_Iin0fkD9Xfqo73JMUQ0E01FdJvV0Wf3Nx-AfJ5AFABKVugUEESK5e0fWnYMVchpz9JT5X97czaqMCunCdRS_xO7Er2FRnwUpI7kNBdoAktpeBh4pKmAR4IfAvmMdhwdi93e9qEROaLfbgOoce9-rtR9wDUUjfrPT7nbzv8WcL_YMhV5QNnGJCRZIYH37qIhvv-y5TKW68pFnRaGGFq-oY1I1r8YzFYgGAZRusESKnge43b4pcFhEFvTLczD01uoG8afW-Wkko3ggJsm4k6zTuUIpTl1sKUQdf7AzuFDNRThxOuAAAAAV4JmhgA"
FORCESUB = config("FORCESUB", default=None)
AUTH = 5872654872

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
