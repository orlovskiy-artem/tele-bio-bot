"""import flask
from telebot import types
from main import *
from constants import *
import os

server = flask.Flask(__name__)



@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, token))
    return "Hello from Heroku!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

"""
