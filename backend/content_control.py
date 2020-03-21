import os
from telegram import Bot

TOKEN = os.environ.get('TELEGRAM_TOKEN')


class TelegramBot:
    def notify(self, restaurant):
        self.bot.send_message(text=restaurant["link"], chat_id=-1001467998540)

    def __init__(self):
        if not TOKEN: return

        self.bot = Bot(token=TOKEN)
