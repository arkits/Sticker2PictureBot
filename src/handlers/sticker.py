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


def handle(bot, update):
    # Handle all stickers received
    start_time = time.time()
    logger.info('Received Sticker Message:')
    logger.info(update.message)

    # Extract file_id from update.message
    update_message_json = update.message
    sticker_json = update_message_json['sticker']
    file_id = sticker_json['file_id']

    # Download and save the sticker
    sticker_file = bot.get_file(file_id)
    sticker_file.download('sticker.webp')

    # Convert sticker.webp to jpg
    sticker_img = Image.open("sticker.webp")
    sticker_img.save("sticker.png", "PNG")

    # Reply with sticker
    logger.info('Replied sticker.png')
    logger.info('--- Took %s seconds ---' % (time.time() - start_time))

    update.message.reply_document(
        document=open('sticker.png', 'rb'), timeout=5000)
