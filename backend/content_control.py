from telegram.ext import Updater

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import telegram
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN')


class TelegramBot:
    chat_id = None

    def notify(self, restaurant):
        self.bot.send_message(text=restaurant["link"], chat_id=self.chat_id)

    def _start(self, update, context):
        if self.chat_id:
            return
        self.bot = context.bot
        self.chat_id = update.message.chat.id
        update.message.reply_text("ready!")

    def __init__(self):
        """Start the bot."""

        # Create the Updater and pass it your bot's token.
        updater = Updater(token=TOKEN, use_context=True)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", self._start))

        # Start the Bot
        updater.start_polling()
