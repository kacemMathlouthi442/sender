import asyncio
from aiogram import Bot, Dispatcher, F
import os
from keepalive import keep_alive
from random import randint


keep_alive()
services = ['Marcus','zelle','Email','CIBC','CashApp','ApplePay','PayPal','BankofAmerica','Amazon','Gmail','wellsfargo','Venmo','citizens','Bank','CapitalOne','Coinbase','Afterpay','Visa','MasterCard','Facebook','WhatsApp','Instagram']

bot = Bot(token=os.environ.get('token'))
dp = Dispatcher()

async def main_loop():
    while True:
        try:
            otp = ''
            for i in range(6):
                otp = otp+str(randint(0,9))
            await bot.send_message(chat_id=-1002609367196, text='''📲 DRAGON OTP BOT 📲 ┃ VOUCHES 🐲
➖➖➖➖➖➖
╭  Service Name ➣ '''+services[randint(0,len(services)-1)]+'''
 ⭐ OTP ➣ `'''+otp+'''` ✅
╰  Capture By: \-\-\-\-\-\-\-\-\-\-
 🤖 [BOT](https://t.me/DRAGON_OTPv2_bot)''',parse_mode='MarkdownV2')
        except Exception as e:
            print(f"❌ Error: {e}")
        try:
            otp = ''
            for i in range(6):
                otp = otp+str(randint(0,9))
            await bot.send_message(chat_id='@M9WDOTP_vouches', text='''📲 M9WD OTP BOT 📲 ┃ 𝗩𝗢𝗨𝗖𝗛𝗘𝗦 ☘️
➖➖➖➖➖➖
╭  Service Name ➣ '''+services[randint(0,len(services)-1)]+'''
 ⭐ OTP ➣ `'''+otp+'''` ✅
╰  Capture By: \-\-\-\-\-\-\-\-\-\-
 🤖 [BOT](https://t.me/m9wdottp_bot)''',parse_mode='MarkdownV2')
        except Exception as e:
            print(f"❌ Error: {e}")
        await asyncio.sleep(randint(300, 900))


if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except KeyboardInterrupt:
        print("Stopped by user.")
