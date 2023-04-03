from aiogram import types

TOKEN = "your token"
if not TOKEN:
    exit('Error: token not found!')

COMMANDS = [
    types.BotCommand('start', 'Стартуем!'),
    types.BotCommand('help', 'Помощь')
]