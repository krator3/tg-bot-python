from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from asyncio import sleep

# Initializing the bot and dispatcher
# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Creating a keyboard, adding buttons
# Создаём клавиатуру, добавляем кнопки
button_linux = KeyboardButton("🐧Linux🐧")
button_cube = KeyboardButton("🎲Бросить кубик🎲")
kb_bot = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bot.add(button_linux, button_cube)

# Start function: greets the user, turns on the keyboard
# Функция старт: приветствует пользователя, включает клавиатуру
@dp.message_handler(commands=["start"])
async def cmd_start(msg: types.Message):
    await msg.answer("Добро пожаловать!", reply_markup=kb_bot)

# Echo function for GIF
# Эхо-функция для GIF
@dp.message_handler(content_types=["animation"])
async def echo_gif(msg:types.Message):
    await msg.reply_animation(msg.animation.file_id)

# Echo function for photos
# Эхо-функция для фото
@dp.message_handler(content_types=["photo"])
async def echo_photo(msg:types.Message):
    await msg.reply_photo(msg.photo[-1].file_id)

@dp.message_handler()
async def bot_func(msg: types.Message):
    if msg.text == "🐧Linux🐧":
        # when you click on the button, a penguin emoji is sent
        #при нажатии на кнопку отправляется эмодзи - пингвин
        await msg.answer("🐧")
    elif msg.text == ("🎲Бросить кубик🎲"):
        #when you click on the button, a cube game with a bot starts
        # при нажатии на кнопку запускается игра в куб с ботом
        await msg.answer("Игра началась!")
        await sleep(4)
        await msg.answer("Куб бота:")
        bot_cube = await msg.answer_dice()
        bot_cube = bot_cube["dice"]["value"]
        await sleep(5)
        await msg.answer("Ваш куб:")
        user_cube = await msg.answer_dice()
        user_cube = user_cube["dice"]["value"]
        await sleep(5)
        if bot_cube>user_cube:
            await msg.answer("Вы проиграли!")
        if bot_cube<user_cube:
            await msg.answer("Вы победили!")
        if bot_cube==user_cube:
            await msg.answer("Ничья!")
    else:
        # Echo function for text
        # Эхо-функция для текста
         await msg.answer(msg.text)

# Launching the bot
# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp)