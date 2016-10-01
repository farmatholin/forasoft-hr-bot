import flask
import telebot
import logging

import time
from bot import hr_bot
import config

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

app = flask.Flask(__name__)


## Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


# Process webhook calls
@app.route(config.WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_json()
        update = telebot.types.Update.de_json(json_string)
        hr_bot.process_new_messages([update.message])
        return ''
    else:
        flask.abort(403)

# Remove webhook, it fails sometimes the set if there is a previous webhook
hr_bot.remove_webhook()

time.sleep(3)

hr_bot.set_webhook(url=config.WEBHOOK_URL_BASE + config.WEBHOOK_URL_PATH,
                certificate=open(config.WEBHOOK_SSL_CERT, 'r'))

# Start flask server
app.run(host=config.WEBHOOK_LISTEN,
        port=config.WEBHOOK_PORT,
        ssl_context=(config.WEBHOOK_SSL_CERT, config.WEBHOOK_SSL_PRIV),
        debug=True)