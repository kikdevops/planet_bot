from flask import Flask, request, json
from settings import *
import messageHandler
from operators_system import Operator


app = Flask(__name__)
operator = Operator()

@app.route('/')
def hello_world():
    return 'Hello from Planeta!'

@app.route('/', methods=['POST'])
def processing():

    operator.id = operator_tokens
    user_token = operator.id

    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        messageHandler.create_answer(data['object'], token)
        return 'ok'
    elif data['type'] == 'group_join':
        messageHandler.create_hello(data['object'], user_token)
        return 'ok'

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
