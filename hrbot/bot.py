import telebot
import config
from hrbot.message_processor import process_message

hr_bot = telebot.TeleBot(config.BOT_TOKEN)

user = hr_bot.get_me()


# Handle '/start'
@hr_bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    response_text = """Привет! Я - официальный Telegram-HRbot от компании Fora Soft\n
Я расскажу вам обо всех открытых вакансиях и отвечу на часто задаваемые вопросы о компании.\n
Официальный сайт - fora-soft.com
HR портал - hrportal.fora-soft.com\n
Fora softwith <3
"""
    hr_bot.send_message(chat_id, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['help'])
def send_welcome(message):
    chat_id = message.chat.id
    response_text = """/start Ну ты понял.....
/help ты и так тут..
/вкансии список вакансий
/info информация по компании
/contacts контакты
"""

    hr_bot.send_message(chat_id, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['contacts'])
def send_welcome(message):
    chat_id = message.chat.id
    response_text = """Наш адрес: Большая пушкарская, 22, Офис 502, г. Санкт-Петербург, Россия, 197198\n
HR отдел: +7 (911) 191-48-63  (с 9:00 до 18:00 по будним дням)
"""
    hr_bot.send_message(chat_id, response_text)
    hr_bot.send_location(chat_id, 59.9581403, 30.3003596)

# Handle all other messages
@hr_bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    chat_id = message.chat.id
    message_text = process_message(message.text)
    hr_bot.send_message(chat_id, message_text)
