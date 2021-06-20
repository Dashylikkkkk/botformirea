import random
print(random.randint(0, 100))
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = types.KeyboardButton('Помощь')
button_2 = types.KeyboardButton('Гороскоп')
button_3 = types.KeyboardButton('Вероятность')
button_4 = types.KeyboardButton('Голос')
markup.add(button_1, button_2, button_3, button_4)