import flask
import telebot
import logging
from bot import hr_bot
import config

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


@app.route(config.WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().encode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        hr_bot.process_new_messages([update.message])
        return ''
    else:
        flask.abort(403)


def getApp():
    return app


# hr_bot.polling(none_stop=False, interval=0, timeout=20)

# Remove webhook, it fails sometimes the set if there is a previous webhook
# hr_bot.remove_webhook()

# Set webhook
hr_bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH,
                   certificate=open(config.WEBHOOK_SSL_CERT, 'r'))

# Start flask server
app.run(host=config.WEBHOOK_LISTEN,
        port=config.WEBHOOK_PORT,
        ssl_context=(config.WEBHOOK_SSL_CERT, config.WEBHOOK_SSL_PRIV),
        debug=True)
