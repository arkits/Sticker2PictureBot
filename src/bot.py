"""
Sticker2Picture
Archit Khode
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import InlineQueryHandler, CallbackQueryHandler
from PIL import Image
import logging
import config
import time
import pyfiglet
from uuid import uuid4
from telegram.utils.helpers import escape_markdown
import handlers.sticker as sticker_handler
import handlers.defaults as defaults_handler
import handlers.perference as perference_handler
import users_util

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
    dp.add_handler(CommandHandler('start', perference_handler.send_perferences))
    dp.add_handler(CommandHandler('help', defaults_handler.help))
    dp.add_handler(CommandHandler('perfs', perference_handler.send_perferences))

    # regular messages
    dp.add_handler(MessageHandler(Filters.text, defaults_handler.all_text))
    dp.add_handler(MessageHandler(Filters.sticker, sticker_handler.handle))

    dp.add_handler(CallbackQueryHandler(perference_handler.update_perference))

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
