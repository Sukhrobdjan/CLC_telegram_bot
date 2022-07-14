from telegram import CallbackQuery, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

buttons = ReplyKeyboardMarkup([['Taksist','Yo`lovchi'], ['Aloqa']], resize_keyboard=True)
direct = ReplyKeyboardMarkup([['Toshkent-Navoiy','Taoshkent-Samarqand'], ['Toshkent-Jizzax','Taoshkent-Buxoro'],['Toshkent-Andijon','Taoshkent-Farg`ona'],['Ortga '], ], resize_keyboard=True)



def start(update:Updater, context:CallbackQuery):
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.username
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAEFRONiz8kpsa6NG5XPVl1qEEDLdC4B6QACWxkAApITQEg3UQr5oSE8nykE')
    update.message.reply_text(
        f'Assalomu alaykum, {first_name}\n @{last_name} \n \n quydagi bo`limlardan birini tanlang 👇👇👇👇👇👇', reply_markup=buttons)
    return 1


def taksist(update:Updater, context:CallbackQuery):
    context.bot.send_message(chat_id = update.message.chat_id, text = 'Yo`nalishni tanlang👇👇',reply_markup =direct)
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAEFRP1iz8_1hK5bqKV-O0dlCjyRgkRZ1gACgw8AAuSr-UubVSA1Q28HDykE')




def yulovchi(update:Updater, context:CallbackQuery):
    context.bot.send_message(chat_id = update.message.chat_id, text = 'Yo`nalishni tanlang',reply_markup =direct)
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAEFRP1iz8_1hK5bqKV-O0dlCjyRgkRZ1gACgw8AAuSr-UubVSA1Q28HDykE')



def aloqa(update:Updater, context:CallbackQuery):
    context.bot.send_message(chat_id = update.message.chat_id, text = '',reply_markup =direct)
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgEAAxkBAAEFRQFiz9CPJ-8tsjyiriACfJyLeWJB5AACJgEAAjgOghFsuLJgLC4WcykE')



def ortga(update:Updater, context:CallbackQuery):
    context.bot.send_message(chat_id = update.message.chat_id, text = 'Kerakli  bo`limni tanlang',reply_markup =buttons)





    

updater = Updater('2108109066:AAHcl8g2qL5j8ID0MkkCGbc8IRUwfwdX6Ck', use_context=True)
conv_handler = ConversationHandler(
    entry_points = [CommandHandler('start', start)],

    states={
        1: [MessageHandler(Filters.regex('^(Taksist)$'), taksist),
            MessageHandler(Filters.regex('^(Yo`lovchi)$'), yulovchi),
            MessageHandler(Filters.regex('^(Aloqa)$'), aloqa),
            MessageHandler(Filters.regex('^(Ortga)$'), ortga),
            ],
        # 2: [MessageHandler(Filters.regex('^(Ortga)$'), taksist),
        #     ],
        
    },
    fallbacks=[MessageHandler(Filters.text, start)]
)

updater.dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()