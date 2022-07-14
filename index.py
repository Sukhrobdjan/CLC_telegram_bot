from ntpath import join
from unittest import result
from urllib import response
from telegram.ext import Updater, CommandHandler,CallbackContext
from telegram.update import Update 
import requests

def hello(update:Update, context:CallbackContext):
    update.message.reply_text(
        'hello {}'.format(update.message.from_user.first_name)
    )

def search(update, context):
    args = context.args
    search_text = ' '.join(args)
    requests.get('https://ru.wikipedia.org/w/index.php',{
        'action':'opensearch',
        'search':search_text,
        'limit':1,
        'namespace':0,
        'format':'json',
    })

    result = response.json()[3]
    update.message.replay_text(

    )

updater = Updater('2108109066:AAHcl8g2qL5j8ID0MkkCGbc8IRUwfwdX6Ck',use_context=True)
updater.dispatcher.add_handler(CommandHandler('start',hello))

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', hello))
dispatcher.add_handler(CommandHandler('search', search))

updater.start_polling()
updater.idle()