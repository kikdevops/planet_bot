import bot.command_system as command_system

def hot():
   message = 'Едь на дачу кусок мяса.'
   return message, ''

hot_command = command_system.Command()

hot_command.keys = ['горячее предложение','hot','куда поехать']
hot_command.description = 'Едь на дачу кусок мяса'
hot_command.process = hot
