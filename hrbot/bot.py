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
From Fora soft with <3
"""
    hr_bot.send_message(chat_id, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    response_text = """/start Ну ты понял.....
/vacancies вакансии
/help ты и так тут..
/about_us информация по компании
/contacts контакты
/we_offer условия работы
"""

    hr_bot.send_message(chat_id, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['about_us'])
def send_about_us(message):
    chat_id = message.chat.id
    response_text = """Мы в Фора Софт дополняем реальность, распознаем объекты на видео, запускаем интернет ТВ,\
разрабатываем платформы для видеонаблюдения, телемедицины и удаленного обучения. \
Наша специализация — мультимедиа приложения.
\nПроекты, которые мы сделали: http://forasoft.com/portfolio/en/
Моменты из нашей жизни: https://www.instagram.com/fora_soft
Последние новости из нашей сферы: https://twitter.com/forasoft
"""

    hr_bot.send_message(chat_id, response_text)
    response_text = """/start Ну ты понял.....
/vacancies вакансии
/help ты и так тут..
/about_us информация по компании
/contacts контакты
/we_offer условия работы
"""

    hr_bot.send_message(chat_id, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['contacts'])
def send_contacts(message):
    chat_id = message.chat.id
    response_text = """Наш адрес: Большая пушкарская, 22, Офис 502, г. Санкт-Петербург, Россия, 197198\n
HR отдел: +7 (911) 191-48-63  (с 9:00 до 18:00 по будним дням)
"""
    hr_bot.send_message(chat_id, response_text)
    hr_bot.send_location(chat_id, 59.9581403, 30.3003596)


@hr_bot.message_handler(commands=['about_us'])
def send_offer(message):
    chat_id = message.chat.id
    response_text = """У нас вы получаете:\n
Стабильность - достойная и стабильная зарплата с пересмотром не реже, чем раз в полгода, официальное трудоустройство,
Социальный пакет: медицинское страхование, обучение, корпоративные мероприятия.
Развитие – интересная работа (у нас нет рутинной поддержки систем на давно устаревших технологиях), \
профессиональный и карьерный рост, новые технологии, превосходные условия труда - отличный коллектив, уютный офис в \
бизнес-центре класса А, гибкий график и совмещение работы и учебы.
"""

    hr_bot.send_message(chat_id, response_text)


@hr_bot.message_handler(commands=['vacancies'])
def send_offer(message):
    chat_id = message.chat.id
    response_text = """Тут пока ничего нет, но мы тебе обещаем, что для тебя обязательно что-то найдём!!"""

    hr_bot.send_message(chat_id, response_text)


# Handle all other messages
@hr_bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    chat_id = message.chat.id
    message_text = process_message(message.text)
    hr_bot.send_message(chat_id, message_text)
