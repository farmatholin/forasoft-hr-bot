import telebot
import config

hr_bot = telebot.TeleBot(config.BOT_TOKEN)


@hr_bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    hr_bot.reply_to(message, "Howdy, how are you doing?")


@hr_bot.message_handler(func=lambda message: True)
def echo_all(message):
    hr_bot.reply_to(message, message.text)

