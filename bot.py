import telebot
import config

hr_bot = telebot.TeleBot(config.BOT_TOKEN)


# Handle '/start' and '/help'
@hr_bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    hr_bot.reply_to(message,
                    ("Hi there, I am EchoBot.\n"
                     "I am here to echo your kind words back to you."))


# Handle all other messages
@hr_bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    hr_bot.reply_to(message, message.text)
