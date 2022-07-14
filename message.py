from telegram.ext import Updater,CallbackContext,CommandHandl
from telegram.update import Update


updater = Updater(token='2108109066:AAHcl8g2qL5j8ID0MkkCGbc8IRUwfwdX6Ck')


def start(update:Update, context:CallbackContext):
    update.message.reply_text('Salom')
    context.bot.send_message(chat_id = update.message.chat_id, text = 'Salom yanna ')   

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start',start))



updater.start_polling()
updater.idle()