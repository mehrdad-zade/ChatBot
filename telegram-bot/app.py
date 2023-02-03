'''
# pip install python-telegram-bot
myToken = 'xyz' #get it form Telegram's BotFather
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

bot = telegram.Bot(token=myToken)
updater = Updater(token=myToken, use_context=True) 
dispatcher = updater.dispatcher

#sends the desired text message through the bot
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

#use a CommandHandler to register it in the dispatcher. bind the / hello command with the hello () function
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)    

#To start our bot
updater.start_polling()

'''
#note: run this app and go to your telegram bot and test it by running start, or hello. other strings will return back the same text.
BOT_TOKEN = 'xyz' #get it form Telegram's BotFather
#pip install pyTelegramBotAPI
import telebot

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)    

#run
bot.infinity_polling()    