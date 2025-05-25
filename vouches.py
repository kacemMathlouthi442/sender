import asyncio
from aiogram import Bot
import os
from keepalive import keep_alive
from random import randint

keep_alive()

services = [
    'Marcus','zelle','Email','CIBC','CashApp','ApplePay','PayPal',
    'BankofAmerica','Amazon','Gmail','wellsfargo','Venmo','citizens',
    'Bank','CapitalOne','Coinbase','Afterpay','Visa','MasterCard',
    'Facebook','WhatsApp','Instagram'
]

bot = Bot(token=os.environ.get('token'))

async def main_loop():
    while True:
        try:
            otp = ''.join([str(randint(0, 9)) for _ in range(6)])
            service = services[randint(0, len(services)-1)]
            msg1 = (
                f"📲 DRAGON OTP BOT 📲 ┃ VOUCHES 🐲\n"
                f"➖➖➖➖➖➖\n"
                f"╭  Service Name ➣ {service}\n"
                f"⭐ OTP ➣ `{otp}` ✅\n"
                f"╰  Capture By: ---------\n"
                f"🤖 [BOT](https://t.me/DRAGON_OTPv2_bot)"
            )
            await bot.send_message(chat_id=-1002609367196, text=msg1, parse_mode='MarkdownV2')
        except Exception as e:
            print(f"❌ Error sending to channel 1: {e}")

        try:
            otp = ''.join([str(randint(0, 9)) for _ in range(6)])
            service = services[randint(0, len(services)-1)]
            msg2 = (
                f"📲 M9WD OTP BOT 📲 ┃ 𝗩𝗢𝗨𝗖𝗛𝗘𝗦 ☘️\n"
                f"➖➖➖➖➖➖\n"
                f"╭  Service Name ➣ {service}\n"
                f"⭐ OTP ➣ `{otp}` ✅\n"
                f"╰  Capture By: ---------\n"
                f"🤖 [BOT](https://t.me/m9wdottp_bot)"
            )
            await bot.send_message(chat_id='@M9WDOTP_vouche', text=msg2, parse_mode='MarkdownV2')
        except Exception as e:
            print(f"❌ Error sending to channel 2: {e}")

        await asyncio.sleep(randint(300, 900))


if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except KeyboardInterrupt:
        print("Stopped by user.")
