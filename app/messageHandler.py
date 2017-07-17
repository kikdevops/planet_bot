import vkapi
import os
import importlib
from command_system import command_list

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(body):
	#default_message
    message = "Прости, кожаный мешок, не понимаю тебя."
    attachment = ''
    for c in command_list:
        if body in c.keys:
            message, attachment = c.process()
    return message, attachment

def create_hello(data, user_token):
	user_id = data['user_id']
#	message = get_hello()
	message = 'Ну что, кусок мяса, вступил?'
	vkapi.send_message(user_id, user_token, message)


def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message = get_answer(data['body'].lower())
   vkapi.send_message(user_id, token, message)