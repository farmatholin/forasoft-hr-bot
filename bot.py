import telebot
import config

hr_bot = telebot.TeleBot(config.BOT_TOKEN)


# Handle '/start'
@hr_bot.message_handler(commands=['start'])
def send_welcome(message):
    response_text = """
    Привет, компания fora soft приветствует тебя.\n
    Как мы могли уже заметить, у тебя накопилось много вопросов, не стесняйся, спрашивай.\n
    with <3 Fora soft
    """
    hr_bot.reply_to(message, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['help'])
def send_welcome(message):
    response_text = """
    /mama mama
    /papa
    """
    hr_bot.reply_to(message, response_text)


# Handle all other messages
@hr_bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    hr_bot.reply_to(message, message.text)
