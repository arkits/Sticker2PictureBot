"""
Sticker2Picture
Archit Khode
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from PIL import Image
import logging
import config
import time
import users_util

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
    logger.info('Converted sticker.png')
    logger.info('--- Took %s seconds ---' % (time.time() - start_time))

    tg_id = update.message.from_user['id']

    user = users_util.get_user(tg_id)

    if user is None:
        delivery_type = "image"
    else:
        delivery_type = user.delivery_perference

    if delivery_type == "image":
        update.message.reply_photo(photo=open('sticker.png', 'rb'), timeout=5000)
    elif delivery_type == "document":
        update.message.reply_document(document=open('sticker.png', 'rb'), timeout=5000)
