import os
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler

TOKEN = os.environ.get('TELEGRAM_TOKEN')


class TelegramBot:
    def notify(self, restaurant, rid):
        keyboard = [[InlineKeyboardButton("Block", callback_data='BLOCK:' + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        self.bot.send_message(text=restaurant["link"], chat_id=-1001467998540, reply_markup=reply_markup)

    def block(self, update, ctx):
        print(update)
        query = update.callback_query
        rid = query.data.split("BLOCK:")[1]

        # TODO block in DB

        keyboard = [[InlineKeyboardButton("Unblock", callback_data='UNBLOCK:' + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text("Now blocked: " + query.message.text, reply_markup=reply_markup)

    def unblock(self, update, ctx):
        query = update.callback_query
        rid = query.data.split("UNBLOCK:")[1]

        # TODO unblock in DB

        keyboard = [[InlineKeyboardButton("Block", callback_data='BLOCK:' + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text("TODO load restaurant link", reply_markup=reply_markup)

    def __init__(self, collection):
        if not TOKEN: return

        self.collection = collection

        updater = Updater(TOKEN, use_context=True)
        self.bot = updater.bot

        updater.dispatcher.add_handler(CallbackQueryHandler(self.block, pattern=r'^BLOCK:'))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.unblock, pattern=r'^UNBLOCK:'))

        updater.start_polling()
