#!/usr/bin/env python

import telegram
from flask import Flask, request

app = Flask(__name__)

global bot
bot = telegram.Bot(token='375084271:AAEguAYJ51fb4HxooL3a7RJp_vGUJ9xR0xY')


@app.route('/HOOK', methods=['POST'])
def webhook_handler():
    print "Method: " + request.method
    if request.method == "POST":
        msg = request.data
        print "Message: " + str(msg)
        # retrieve the message in JSON and then transform it to Telegram object
        # update = telegram.Update.de_json(request.get_json(force=True))

        #chat_id = update.message.chat.id

        # Telegram understands UTF-8, so encode text for unicode compatibility
        #text = update.message.text.encode('utf-8')

        # repeat the same message back (echo)
        #bot.sendMessage(chat_id=chat_id, text=text)

    return 'ok'


@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('https://URL/HOOK')
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
