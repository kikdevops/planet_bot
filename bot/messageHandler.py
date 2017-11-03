import bot.vkapi as vkapi
import os
import importlib
from bot.command_system import command_list
from bot.settings import bye_message, hello_message

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("bot/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       print("commands." + m[0:-3])
       importlib.import_module("bot.commands." + m[0:-3])

def get_answer(body):
	#default_message
    message = "Пожалуйста подождите, мы приступили к обработке вашего запроса."
    attachment = ''
    for c in command_list:
        if body in c.keys:
            message, attachment = c.process()
    return message, attachment

def create_hello(data, user_token):
  user_id = data['user_id']
  user_data = vkapi.get_user_data(user_id)
  message = hello_message.format(name = user_data[0]['first_name'])
  vkapi.send_message(user_id, user_token, message)

def create_bye(data, user_token):
  user_id = data['user_id']
  message = bye_message
  vkapi.send_message(user_id, user_token, message)


def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message = get_answer(data['body'].lower())
   vkapi.send_message(user_id, token, message)
