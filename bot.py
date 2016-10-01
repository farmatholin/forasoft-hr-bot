import telebot
import config

hr_bot = telebot.TeleBot(config.BOT_TOKEN)

user = hr_bot.get_me()

# Handle '/start'
@hr_bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    response_text = """
    Привет, компания fora soft приветствует тебя.
Как мы могли уже заметить, у тебя накопилось много вопросов, не стесняйся, спрашивай.
with <3 Fora soft
"""
    hr_bot.send_message(chat_id, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['help'])
def send_welcome(message):
    chat_id = message.chat.id
    response_text = """/mama mama
/papa
"""

    hr_bot.send_message(chat_id, response_text)


# Handle all other messages
@hr_bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    chat_id = message.chat.id
    hr_bot.send_message(chat_id, message.text)
