import os
from bson.objectid import ObjectId
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler
from db import collection

TOKEN = os.environ.get('TELEGRAM_TOKEN')


class TelegramBot:
    def notify(self, restaurant, rid):
        keyboard = [[InlineKeyboardButton("Block", callback_data='BLOCK:' + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        self.bot.send_message(text=restaurant["link"], chat_id=-1001467998540, reply_markup=reply_markup)

    def block(self, update, ctx):
        query = update.callback_query
        rid = query.data.split("BLOCK:")[1]

        collection.update_one({'_id': ObjectId(rid)}, {'$set': {'blocked': True}})
        restaurant = collection.find_one({'_id': ObjectId(rid)})

        keyboard = [[InlineKeyboardButton("Unblock", callback_data='UNBLOCK:' + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text("Now blocked: " + restaurant["link"], reply_markup=reply_markup)

    def unblock(self, update, ctx):
        query = update.callback_query
        rid = query.data.split("UNBLOCK:")[1]

        collection.update_one({'_id': ObjectId(rid)}, {'$set': {'blocked': False}})
        restaurant = collection.find_one({'_id': ObjectId(rid)})

        keyboard = [[InlineKeyboardButton("Block", callback_data='BLOCK:' + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text(restaurant["link"], reply_markup=reply_markup)

    def __init__(self, webhook=False):
        if not TOKEN: return

        if webhook:
            updater = Updater(TOKEN, use_context=False)
            self.bot = updater.bot
            updater.dispatcher.add_handler(CallbackQueryHandler(self.block, pattern=r'^BLOCK:'))
            updater.dispatcher.add_handler(CallbackQueryHandler(self.unblock, pattern=r'^UNBLOCK:'))
            updater.start_webhook(webhook_url='https://weinretter.de/bot', port=5001)
            print("HERE")
        else:
            self.bot = Bot(TOKEN)


if __name__ == '__main__':
    TelegramBot(webhook=True)
