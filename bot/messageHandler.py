import bot.vkapi as vkapi
import os
import importlib
from bot.command_system import command_list

def load_modules():
   # путь от рабочей директории, ее можно изменить в настройках приложения
   files = os.listdir("commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       print("commands." + m[0:-3])
       importlib.import_module("commands." + m[0:-3])

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
  message = '''Мы рады приветствовать вас в группе путешественников!\n
               Если у вас возникнут какие либо вопросы вы всегда можете их задать в сообщениях для группы.\n
               Если вы хотите ознакомится с горячими предложениями напишите 'куда поехать' в чат сообщества.'''

#  message = user_token
  vkapi.send_message(user_id, user_token, message)


def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message = get_answer(data['body'].lower())
   vkapi.send_message(user_id, token, message)
