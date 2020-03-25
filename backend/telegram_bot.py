import os
from bson.objectid import ObjectId
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler
from db import collection

TOKEN = os.environ.get("TELEGRAM_TOKEN")


class TelegramBot:
    def notify(self, rid, link, name):
        keyboard = [[InlineKeyboardButton("Block", callback_data="BLOCK:" + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        self.bot.send_message(
            text=f"Registration:\n{name}\n{link}",
            chat_id=-1001467998540,
            reply_markup=reply_markup,
        )

    def block(self, update, ctx):
        print("new block request")
        query = update.callback_query
        try:
            rid = query.data.split("BLOCK:")[1]

            collection.update_one({"_id": ObjectId(rid)}, {"$set": {"blocked": True}})
            restaurant = collection.find_one({"_id": ObjectId(rid)})

            keyboard = [
                [InlineKeyboardButton("Unblock", callback_data="UNBLOCK:" + str(rid))]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)

            query.edit_message_text(
                "Now blocked: " + restaurant["link"], reply_markup=reply_markup
            )
        except Exception:
            query.edit_message_text("Error")

    def unblock(self, update, ctx):
        query = update.callback_query
        rid = query.data.split("UNBLOCK:")[1]

        collection.update_one({"_id": ObjectId(rid)}, {"$set": {"blocked": False}})
        restaurant = collection.find_one({"_id": ObjectId(rid)})

        keyboard = [[InlineKeyboardButton("Block", callback_data="BLOCK:" + str(rid))]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        query.edit_message_text(restaurant["link"], reply_markup=reply_markup)

    def __init__(self, webhook=False):
        if not TOKEN:
            return

        if webhook:
            updater = Updater(TOKEN, use_context=True)
            self.bot = updater.bot
            updater.dispatcher.add_handler(
                CallbackQueryHandler(self.block, pattern=r"^BLOCK:")
            )
            updater.dispatcher.add_handler(
                CallbackQueryHandler(self.unblock, pattern=r"^UNBLOCK:")
            )
            updater.start_webhook(url_path="/bot", listen="0.0.0.0", port=5001)
            self.bot.set_webhook(url="https://weinretter.de/bot")
        else:
            self.bot = Bot(TOKEN)


if __name__ == "__main__":
    t = TelegramBot(webhook=True)
    from threading import Event

    Event().wait()
