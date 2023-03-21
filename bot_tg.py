from config import TOKEN
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from asyncio import sleep

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

button_linux = KeyboardButton("🐧Linux🐧")
button_cube = KeyboardButton("🎲Бросить кубик🎲")
kb_bot = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_bot.add(button_linux, button_cube)

@dp.message_handler(commands=["start"])
async def cmd_start(msg: types.Message):
    await msg.answer("Добро пожаловать!", reply_markup=kb_bot)


@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text == "🐧Linux🐧":
        await msg.answer("🐧")
    elif msg.text == ("🎲Бросить кубик🎲"):
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
        await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)