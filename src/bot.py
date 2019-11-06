"""
Sticker2Picture
Archit Khode
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import logging
import config
import time
import pyfiglet

import handlers.sticker as sticker_handler
import handlers.defaults as defaults_handler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    # Start the bot...

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config.tg_bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # /commands
    dp.add_handler(CommandHandler('start', defaults_handler.start))
    dp.add_handler(CommandHandler('help', defaults_handler.help))

    # regular messages
    dp.add_handler(MessageHandler(Filters.text, defaults_handler.all_text))
    dp.add_handler(MessageHandler(Filters.sticker, sticker_handler.handle))

    dp.add_error_handler(defaults_handler.error)
    logger.debug('Added handlers...')

    # Gotta look more 1337!
    ascii_banner = pyfiglet.figlet_format("Sticker2Picture")
    print(ascii_banner)

    # Start the Bot
    updater.start_polling()
    logger.info('Started polling...')
    logger.info('--------')

    updater.idle()


if __name__ == '__main__':
    main()
