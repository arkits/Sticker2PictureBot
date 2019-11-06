"""
Sticker2Picture
Archit Khode
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import logging
import config
import time

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    # Handle /start
    logger.info('Responding /start {}'.format(update.message))
    update.message.reply_text('🙏 NAMASKAR MANDALI 🙏')


def help(bot, update):
    # Handle /help
    logger.info('Responding /help - {}'.format(update.message))
    update.message.reply_text('Send me a Telegram Sticker and I will send you sticker as a picture!')


def all_text(bot, update):
    # Handle all text messages received
    logger.info('Received Text Message: {}'.format(update.message))
    update.message.reply_text("Please send me a sticker...")


def error(bot, update, error):
    # Log erros in update obj
    logger.warning('Update "%s" caused error "%s"', update, error)
