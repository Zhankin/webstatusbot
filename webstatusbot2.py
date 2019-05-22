import telegram
#import telebot
#from telebot import types
#from telegram import ReplyMarkup
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler,ConversationHandler)

#bot = telebot.TeleBot('662816784:AAHRzBAXtllAgb99yJZKb55RRO34fQN4mxQ')

#@bot.message_handler(commands=['start'])
EMPLOYEES, EMPLOYEES2, EMPLOYEES3 = range(3)
def start(bot,update):
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True)
        reg_button = types.KeyboardButton(text="Share my contact", request_contact=True)
        keyboard.add(reg_button)
        update.message.reply_text("Please share your contact", reply_markup=keyboard)
        return EMPLOYEES

def emp_group(bot,update,user_data):
        update.message.reply_text("Hello collegue!")
def emp_group2(bot,update,user_data):
        update.message.reply_text("Hello collegue!")
def emp_group3(bot,update,user_data):
        update.message.reply_text("Hello collegue!")


def done(bot, update, user_data):
    update.message.reply_text("Bye")
    user_data.clear()
    return ConversationHandler.END
#@bot.message_handler(content_types=['contact'])
#def contact_handler(message):
#    print(message.contact.phone_number)

#bot.polling(none_stop=True, interval=0)

if __name__ == "__main__":
        try:
                TOKEN='662816784:AAHRzBAXtllAgb99yJZKb55RRO34fQN4mxQ'
                updater = Updater(TOKEN)
                dp = updater.dispatcher
                conv_handler = ConversationHandler(
                        entry_points=[CommandHandler('start', start)],
                        states={
                                EMPLOYEES: [MessageHandler(Filters.text, emp_group, pass_user_data=True),],
                                EMPLOYEES2: [MessageHandler(Filters.text, emp_group2, pass_user_data=True),],
                                EMPLOYEES3: [MessageHandler(Filters.text, emp_group3, pass_user_data=True),],
                        },
                        fallbacks=[RegexHandler('^Done$', done, pass_user_data=True)]
                )
                dp.add_handler(conv_handler)
                updater.start_webhook(listen="0.0.0.0",port=80,url_path=TOKEN,cert='webhook_cert.pem', key='webhook_pkey.key',webhook_url='https://81.211.150.236/'+TOKEN)
                #updater.bot.setWebhook("https://81.211.150.236/",certificate='webhook_cert.pem')
                #updater.start_polling(poll_interval=0.0, timeout=10, clean=False, bootstrap_retries=-1, read_latency=2.0, allowed_updates=None)
                updater.idle()
        except KeyboardInterrupt:
                pass
