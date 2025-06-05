import asyncio
from aiogram import Bot
import os
from keepalive import keep_alive
from random import randint

keep_alive()

services = [
    'Marcus', 'zelle', 'Email', 'CIBC', 'CashApp', 'ApplePay', 'PayPal',
    'BankofAmerica', 'Amazon', 'Gmail', 'wellsfargo', 'Venmo', 'citizens',
    'Bank', 'CapitalOne', 'Coinbase', 'Afterpay', 'Visa', 'MasterCard',
    'Facebook', 'WhatsApp', 'Instagram'
]

# Load token
TOKEN = os.environ.get('token')
if not TOKEN:
    print("❌ Bot token not found in environment!")
    exit()

bot = Bot(token=TOKEN)

async def main_loop():
    while True:
        try:
            otp = ''.join([str(randint(0, 9)) for _ in range(6)])
            service = services[randint(0, len(services)-1)]
            msg1 = (
                f"<b>📲 DRAGON OTP BOT 📲 ┃ VOUCHES 🐲</b>\n"
                f"➖➖➖➖➖➖\n"
                f"╭  Service Name ➣ <b>{service}</b>\n"
                f"⭐ OTP ➣ <code>{otp}</code> ✅\n"
                f"╰  Capture By: ---------\n"
                f"🤖 <a href='https://t.me/DRAGON_OTPv2_bot'>BOT</a>"
            )
            await bot.send_message(chat_id=-1002609367196, text=msg1, parse_mode='HTML')
        except Exception as e:
            print(f"❌ Error sending to channel 1: {e}")


        await asyncio.sleep(randint(300, 900))


if __name__ == "__main__":
    try:
        asyncio.run(main_loop())
    except KeyboardInterrupt:
        print("Stopped by user.")
