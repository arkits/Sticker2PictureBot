"""
Sticker2Picture
Archit Khode
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image
import logging
import config
import time
import users_util
import models.user

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)


def send_perferences(bot, update):

    keyboard = [
        [InlineKeyboardButton("Document", callback_data="document"),
        InlineKeyboardButton("Image", callback_data="image")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        'How do you want to receive the export?', reply_markup=reply_markup)


def update_perference(bot, update):

    delivery_perference = update.callback_query.data

    tg_id = update.callback_query.from_user['id']

    logging.info("Updating perfernce of id={} delivery_perference={}".format(
        tg_id,
        delivery_perference
    ))

    user = users_util.get_user(tg_id)

    if user is None:
        logging.info("New user! - {}".format(tg_id))
        user = models.user.User(tg_id)

    user.delivery_perference = delivery_perference

    users_util.set_user(user)

    update.callback_query.edit_message_text(text="Done! I'll send you stickers as {}".format(delivery_perference))
