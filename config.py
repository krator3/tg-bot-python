from aiogram import types

TOKEN = "6034886553:AAGcITepc9JUHL3LKWk7TgXPGcPqsyxa4Ug"
if not TOKEN:
    exit('Error: token not found!')

COMMANDS = [
    types.BotCommand('start', 'Стартуем!'),
    types.BotCommand('help', 'Помощь')
]