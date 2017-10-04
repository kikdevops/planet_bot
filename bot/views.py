from bot import app
from bot.settings import *
from bot.operators_system import Operator
from flask import request, json
import bot.messageHandler as messageHandler

operator = Operator()

@app.route('/')
def hello_world():
    return 'Hello from Planeta!'

@app.route('/', methods=['POST'])
def processing():

    print(operator_tokens)
    operator.id = operator_tokens
    user_token = operator.id

    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
#    elif data['type'] == 'message_new':
#        messageHandler.create_answer(data['object'], token)
#        return 'ok'
    elif data['type'] == 'group_join':
        messageHandler.create_hello(data['object'], user_token)
        return 'ok'

