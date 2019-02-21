"""
Sticker2Picture
Archit Khode
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import config

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    # Handle /start
    logger.info('Responding /start')
    update.message.reply_text('🙏 NAMASKAR MANDALI 🙏')


def help(bot, update):
    # Handle /help
    logger.info('Responding /help')
    update.message.reply_text('Help!')

def all_text(bot, update):
    # Handle all text messages received
    logger.info('Received Text Message:')
    logger.info(update.message)
    update.message.reply_text("Please send me a sticker...")

def all_stickers(bot, update):
    # Handle all stickers received
    logger.info('Received Sticker Message:')
    logger.info(update.message)

    # Extract file_id from update.message
    update_message_json = update.message
    sticker_json = update_message_json['sticker']
    file_id = sticker_json['file_id']

    # Download and save the sticker
    sticker_file = bot.get_file(file_id)
    sticker_file.download('sticker.webp')

    # Reply with sticker
    update.message.reply_sticker(sticker=file_id)


def error(bot, update, error):
    # Log erros in update obj
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    # Start the bot...

    # Create the EventHandler and pass it your bot's token.
    updater = Updater(config.tg_bot_token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # /commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # regular messages
    dp.add_handler(MessageHandler(Filters.text, all_text))
    dp.add_handler(MessageHandler(Filters.sticker, all_stickers))

    dp.add_error_handler(error)
    logger.debug('Added handlers...')

    # Start the Bot
    updater.start_polling()
    logger.info('Started polling...')

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()