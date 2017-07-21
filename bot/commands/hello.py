import bot.command_system as command_system

def hello():
   message = 'Привет, как дела?\n'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствовать кожаного мешка'
hello_command.process = hello
