# Simple-Echo-Telegram-Bot
*A simple telegram bot that echoes your input using Python 2.7, Flask framework, setWebhook method, and Google App Engine (optional)*

This is a simple telegram bot that echoes your input using Python 2.7, Flask microframework, and setWebhook method ([python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot) package required).

This example shows you how to set up webhook, and how to receive and send a text message.

Please exchange the TOKEN, the webhook URL, and the HOOK path with your own.

Tested on Google App Engine (GAE) with virtualenv enabled. I followed the tutorial in [this Youtube video](https://www.youtube.com/watch?v=FRI3QGNWJYI). Basically you set up virtualenv inside the GAE directory, and then appened the path to it in every script that runs. (Otherwise you get an error in the import.)

* The bot.py file is for general implementation.
* The bot_gae.py file with app.yaml is for Google App Engine. The only difference is the sys.path.appened statement at the top. You may need to edit the virtual environment path accordingly.

## Required
* Python 2.7
* [python-telegram-bot](https://github.com/leandrotoledo/python-telegram-bot) package
* [Flask](http://flask.pocoo.org/) microframework

## How to use
* Install the script
* Visit https://URL/set_webhook in your browser to set up webhook.
* Start chatting in Telegram and enjoy your echoes! :) 