# Boulevard

import config
import logging

from aiogram import Bot, Dispatcher, executor, types
import btns as kb
import markups as nav

import random

logging.basicConfig(level=logging.INFO)

# init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


# functions MAIN
# # !Эхо
# @dp.message_handler()
# async def echo(message: types.Message):
# 	await message.answer(message.text)

# # !фильтр на цензуру
# @dp.message_handler()
# async def filter_messages(message: types.Message):
# 	if "мат" in message.text:
# 		await message.delete()

# # !удаляет "пользователь ... присоединился"
# @dp.message_handler(content_types=["new_chat_members"])
# async def in_user_joined(message: types.Message):
# 	print("SMS DEL")
# 	await message.delete()

# №1 Хэндлер
@dp.message_handler(commands="start")
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет! {0.first_name}".format(message.from_user), reply_markup = nav.mainMenu)

# №2 Хэндлер
async def cmd_test2(message: types.Message):
    await message.reply("Хорошо, сам как?")

# Прописываем команду для №2 хендлера
dp.register_message_handler(cmd_test2, commands="howareyou?")

# №3 Хэндлер
@dp.message_handler()
async def bot_message(message: types.Message):
    # await bot.send_message(message.from_user.id, "Привет! {0.first_name}".format(message.from_user), reply_markup = nav.mainMenu)
    if message.text == 'Рандомное число (0, 100)':
        await bot.send_message(message.from_user.id, 'Ваше рандомное число: ' + str(random.randint(0, 100)))
    
    elif message.text == '<-- Главное':
        await bot.send_message(message.from_user.id, '<-- Главное', reply_markup = nav.mainMenu)
    
    elif message.text == 'Другое':
        await bot.send_message(message.from_user.id, '-->', reply_markup = nav.otherMenu)

    elif message.text == 'Информация':
        await bot.send_message(message.from_user.id, 'Информация')
        
    elif message.text == 'Моя музыка':
        await bot.send_message(message.from_user.id, 'After Dark - Mr. Kitty')

    else:
        await message.reply('Что за xyйню ты несёшь?!')




# Run
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)