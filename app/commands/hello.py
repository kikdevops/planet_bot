import command_system

def hello():
   message = 'Привет, кожаный мешок!\nЯ новый бот-турперелет.'
   return message, ''

hello_command = command_system.Command()

hello_command.keys = ['привет', 'hello', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствовать кожаного мешка'
hello_command.process = hello