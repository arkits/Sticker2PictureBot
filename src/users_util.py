#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode

import logging
import pickle
import random
import models.user
from datetime import datetime

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Using Python pickling for data persistence
try:
    with open('resources/users.pickle', 'rb') as handle:
        users_dict = pickle.load(handle)
        logger.info('Loaded Users pickle')
except:
    logger.info('Users pickle not found... Making new one')
    users_dict = {}
    with open('resources/users.pickle', 'wb') as handle:
        pickle.dump(users_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)


def get_user(tg_id):
    # Get a User based on tg_id

    if tg_id in users_dict:
        user = users_dict[tg_id]
    else:
        user = None

    return user


def set_user(user):
    # Update User and commit to pickle

    users_dict[user.id] = user

    with open('resources/users.pickle', 'wb') as handle:
        pickle.dump(users_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
