#!/usr/bin/env python3

import config
import logging
from telegram.ext import Updater, CommandHandler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
                    %(message)s', level=logging.INFO)


def nuke(bot, update):
    if not update.message:
        return
    m = update.message
    if m.chat.type == "private":
        text = "This bot does not work in PM."
        bot.send_message(chat_id=m.chat_id, text=text)
        return
    if not m.reply_to_message:
        text = "You need to reply to a message."
        bot.send_message(chat_id=m.chat_id, text=text)
        return
    user = bot.get_chat_member(m.chat.id, m.from_user.id)
    if not user.can_delete_messages and user.status != "creator":
        text = ('Only admins with "Delete Messages Permission" are allowed '
                'to /nuke')
        bot.send_message(chat_id=m.chat_id, text=text)
        return
    for i in range(m.reply_to_message.message_id, m.message_id + 1):
        try:
            bot.delete_message(m.chat_id, i)
        except:
            continue


updater = Updater(token=config.api_key)
dispatcher = updater.dispatcher
nuke_handler = CommandHandler('nuke', nuke)
dispatcher.add_handler(nuke_handler)

if config.update_method == "polling":
    updater.start_polling()
elif config.update_method == "webhook":
    updater.start_webhook(listen=config.webhook["listen"],
                          url_path=config.webhook["url_path"],
                          port=config.webhook["port"])
    updater.bot.set_webhook(url=config.webhook["url"])
