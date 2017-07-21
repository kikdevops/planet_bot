from flask import Flask, request, json
from bot.settings import *
import bot.messageHandler


app = Flask(__name__)
from bot import views 

if __name__ == '__main__':
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('planetbot.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('planet bot startup')
    app.run(debug = False)