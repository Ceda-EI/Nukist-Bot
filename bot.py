#!/usr/bin/env python3

import config
import logging
from telegram.ext import Updater, CommandHandler
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - \
                    %(message)s', level=logging.INFO)


def nuke(bot, update):
    pass


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
