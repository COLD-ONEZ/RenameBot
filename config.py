import os
import re

id_pattern = re.compile(r'^.\d+$')
# get a token from @BotFather
TOKEN = os.environ.get("TOKEN", "5944960949:AAFm85Fuk1wpucoFlRU8vCTvl6TVfplMu3I")
# The Telegram API things
APP_ID = int(os.environ.get("APP_ID", "29487476"))
API_HASH = os.environ.get("API_HASH", "f3c3a572ecb00bcd9ba608f21a249218")
#Array to store users who are authorized to use the bot
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5592844994 5329179170 730103880').split()]
#Your Mongo DB Database Name
DB_NAME = os.environ.get("DB_NAME", "coldmoviesbot")
#Your Mongo DB URL Obtained From mongodb.com
DB_URL = os.environ.get("DB_URL", "mongodb+srv://C_M_D:cold_x_movies@coldmoviesbot.ig0bwq1.mongodb.net/?retryWrites=true&w=majority")

START_PIC = (os.environ.get("START_PIC", "https://telegra.ph/file/6866d150c688697901044.jpg https://telegra.ph/file/a2fa6177e5e5dbee6ab58.jpg https://telegra.ph/file/2252e40db931835a311fc.jpg https://telegra.ph/file/76b495e4f484b918e4429.jpg https://telegra.ph/file/37168ba6fe81c145ca294.jpg https://telegra.ph/file/262a830630e0e12deac6e.jpg https://telegra.ph/file/9599d61d4316c873cc8b0.jpg https://telegra.ph/file/701b28453b269a10219d4.jpg https://telegra.ph/file/17a3e2967853eac5efbe4.jpg https://telegra.ph/file/734024f384f2d4fe7ffed.jpg https://telegra.ph/file/65fb8c4d80d970856fd1a.jpg https://telegra.ph/file/8b5abab313ef932e1ebdf.jpg https://telegra.ph/file/58da22073a20edff1bbf3.jpg https://telegra.ph/file/c8e9d1e32a7bf7c2ccc2b.jpg https://telegra.ph/file/5a83b7562e6c585101f68.jpg https://telegra.ph/file/b9f16879f6fb8a25910f7.jpg https://telegra.ph/file/6b24b2ebc7a55c59d3930.jpg https://telegra.ph/file/8f23d4392fd4a5b011b07.jpg https://telegra.ph/file/c7e2e616853185375dcdd.jpg https://telegra.ph/file/b32bb4a593e5950f539cc.jpg")).split()

PORT = os.environ.get("PORT", "8080")

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001899955138")

FLOOD = int(os.environ.get("FLOOD", "5"))
