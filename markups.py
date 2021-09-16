from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Скрыть кнопку после нажатия| one_time_keyboard = True
# Пример| greet_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(btnHi)

btnHi = KeyboardButton("Привет")
greet_kb = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True).add(btnHi)

btnMain = KeyboardButton('<-- Главное')

# Main
btnRandom = KeyboardButton('Рандомное число (0, 100)')
btnOther = KeyboardButton('Другое')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther)


# Other
btnInfo = KeyboardButton('Информация')
btnBTC = KeyboardButton('Курс Биткоин [BTC]')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnBTC, btnMain)