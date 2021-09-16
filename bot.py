# Boulevard

import config
import logging

from aiogram import Bot, Dispatcher, executor, types
import btns as kb

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
@dp.message_handler(commands="hi")
async def cmd_test1(message: types.Message):
    await message.reply("Привет!", reply_markup = kb.greet_kb)

# №2 Хэндлер
async def cmd_test2(message: types.Message):
    await message.reply("Хорошо, сам как?")

# Прописываем команду для №2 хендлера
dp.register_message_handler(cmd_test2, commands="howareyou?")





# Run
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)