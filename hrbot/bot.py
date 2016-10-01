import telebot
import config
from hrbot.message_processor import process_message
from telebot import types

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

/vacancies вакансии
/help список команд
/about_us информация по компании
/contacts контакты
/we_offer условия работы
/instagram фотка из инстаграма
"""
    hr_bot.send_message(chat_id, response_text)


# Handle '/help'
@hr_bot.message_handler(commands=['help'])
def send_help(message):
    chat_id = message.chat.id
    response_text = """/vacancies открытые вакансии
/help помощь
/contacts контакты
/about_us информация о компании
/we_offer условия работы
/instagram фотка из инстаграма
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


# Handle '/help'
@hr_bot.message_handler(commands=['contacts'])
def send_contacts(message):
    chat_id = message.chat.id
    response_text = """Наш адрес: Большая пушкарская, 22, Офис 502, г. Санкт-Петербург, Россия, 197198\n
HR отдел: +7 (911) 191-48-63  (с 9:00 до 18:00 по будним дням)
"""
    hr_bot.send_message(chat_id, response_text)
    hr_bot.send_location(chat_id, 59.9581403, 30.3003596)


@hr_bot.message_handler(commands=['we_offer'])
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
def send_vac(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardMarkup()
    diz = types.KeyboardButton('Дизайн')
    dev = types.KeyboardButton('Разработка')
    markup.row(diz)
    markup.row(dev)
    msg = hr_bot.send_message(chat_id, "Выбери вакансию которая тебя интересует:", reply_markup=markup)
    hr_bot.register_next_step_handler(msg, process_step)


def process_step(message):
    chat_id = message.chat.id
    markup = types.ReplyKeyboardHide(selective=False)
    response_text = ''
    if message.text == "Дизайн":
        response_text = "Strong risovat kartinki chtob mi takie AAAAAH VAI VAI VAI AYVAZOVSKY PRYAM!!!!"
    elif message.text == "Разработка":
        php = types.KeyboardButton('PHP')
        js = types.KeyboardButton('JavaScript')
        markup = types.ReplyKeyboardMarkup()
        markup.row(php)
        markup.row(js)
        response_text = 'Выберите вакансию для получения описания вакансии:'
    else:
        pass
    if message.text == "PHP" or message.text == "JavaScript":
        markup = types.ReplyKeyboardHide(selective=False)
        response_text = "В Git умеешь, тогда ты с нами!"
    msg = hr_bot.send_message(chat_id, response_text, reply_markup=markup)
    hr_bot.register_next_step_handler(msg, process_step)


@hr_bot.message_handler(commands=['instagram'])
def send_instagram(message):
    chat_id = message.chat.id
    photo = open('content/img.jpg', 'rb')
    hr_bot.send_photo(chat_id, photo)


# Handle all other messages
@hr_bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    chat_id = message.chat.id
    message_text = process_message(message.text)
    if message.text == "PHP" or message.text == "JavaScript" or message.text == "Дизайн" or message.text == "Разработка":
        pass
    else:
        hr_bot.send_message(chat_id, message_text)
