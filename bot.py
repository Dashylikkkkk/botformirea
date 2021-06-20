import telebot
from telebot import types
import random

bot = telebot.TeleBot('1886472320:AAEDFLCouorzflf8yKbqqM4f0mfYkVDF5xg')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    name = message.from_user.first_name
    if message.text == '/start':
        item1 = types.KeyboardButton('/help')
        item2 = types.KeyboardButton('/luck')
        item3 = types.KeyboardButton('/zodiac')
        item4 = types.KeyboardButton('Голос')
        item5 = types.KeyboardButton('Купить колбасы')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(item1, item2, item3, item4, item5)
        bot.send_message(message.from_user.id,
                         'Здравствуйте, ' + name + ', я собака в окне, напиши /help, чтобы узнать, какие умные вещи я '
                                                   'умею',
                         reply_markup=markup)
    elif message.text == '/help':
        bot.send_message(message.from_user.id, 'Напиши /zodiac, чтобы посмотреть гороскоп '
                                               '\nНапиши /luck, а затем событие, вероятность которого ты хочешь узнать.'
                                               '\nНапиши "Голос" и посмотри, что будет')
    elif message.text == 'Голос':
        voice(message)
    elif message.text == '/luck':
        luck(message)
    elif message.text == '/zodiac':
        zodiac(message)
    elif message.text == 'Купить колбасы':
        kolbasa(message)
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')


def voice(message):
    global eat
    if message.text == 'Голос':
        if not eat:
            bot.send_message(message.from_user.id, 'купи мне колбасы')
        else:
            bot.send_message(message.from_user.id, 'гав')


eat = False


def kolbasa(message):
    global eat
    if message.text == 'Купить колбасы':
        eat = True
        bot.send_message(message.from_user.id, 'Вы купили собаке колбасы, теперь она сыта.')


def luck(message):
     bot.send_message(message.from_user.id, 'Введи событие, вероятность которого ты хочешь узнать')
     bot.register_next_step_handler(message, probability)
    

def probability(message):
    global rand
    rand = random.randint(0, 100)
    bot.send_message(message.from_user.id, 'Вероятность твоего события равна ' + str(rand) + '%')


def zodiac(message):
     keyboard = types.InlineKeyboardMarkup()
     oven = types.InlineKeyboardButton(text='Овен 21.01-20.04', callback_data='zodiac')
     keyboard.add(oven)
     telec = types.InlineKeyboardButton(text='Телец 21.04-20.05', callback_data='zodiac')
     keyboard.add(telec)
     blizneci = types.InlineKeyboardButton(text='Близнецы 21.05-20.06', callback_data='zodiac')
     keyboard.add(blizneci)
     rak = types.InlineKeyboardButton(text='Рак 21.06-22.07', callback_data='zodiac')
     keyboard.add(rak)
     lev = types.InlineKeyboardButton(text='Лев 23.07-22.08', callback_data='zodiac')
     keyboard.add(lev)
     deva = types.InlineKeyboardButton(text='Дева 23.08-22.09', callback_data='zodiac')
     keyboard.add(deva)
     vesi = types.InlineKeyboardButton(text='Весы 23.09-22.10', callback_data='zodiac')
     keyboard.add(vesi)
     skorpion = types.InlineKeyboardButton(text='Скорпион 23.10-22.11', callback_data='zodiac')
     keyboard.add(skorpion)
     strelec = types.InlineKeyboardButton(text='Стрелец 23.11-21.12', callback_data='zodiac')
     keyboard.add(strelec)
     kozerog = types.InlineKeyboardButton(text='Козерог 22.12-19.01', callback_data='zodiac')
     keyboard.add(kozerog)
     vodoley = types.InlineKeyboardButton(text='Водолей 20.01-19.02', callback_data='zodiac')
     keyboard.add(vodoley)
     ribi = types.InlineKeyboardButton(text='Рыбы 20.02-20.03', callback_data='zodiac')
     keyboard.add(ribi)
     bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)


a = ['Вы способны на многое. Едва ли на пути возникнут преграды, которые вы не сможете преодолеть.',
     'Подходящий день для завершения дел, начатых раньше. Вы правильно расставляете приоритеты, понимаете, на чем нужно'
     ' сосредоточиться, поэтому добиваетесь отличных результатов.', 'Действуйте самостоятельно в первой половине дня. '
     'Так у вас будет гораздо больше шансов добиться успеха. Переговоры и обсуждения отнимают слишком много времени,'
     ' а советы окружающих часто лишь сбивают вас с толку.']
b = ['Вечер будет гораздо благоприятнее для общения, полезно будет побеседовать о каких-то важных вопросах.',
     'Вероятны денежные поступления. Они могут быть незначительными, но окажутся очень кстати.',
     'Вторая половина дня благоприятна для общения с близкими. В это время можно говорить о самых разных вещах, '
     'не опасаясь недопонимания, взаимных обид и претензий.']
c = ['Беспокойный насыщенный день. Каждая минута на счету, ведь вам нужно сделать много полезного и для себя,'
     ' и для других. ',
     'Вторая половина дня будет несколько сложнее. Дело тут не в возникающих проблемах, а в том, что '
     'эмоциональный фон становится более напряженным, любая мелочь заставляет вас волноваться. ',
     'Не исключено начало дружеских отношений или романтической истории. ',
     'Вы нравитесь людям. Часто оказывается достаточно короткого '
     'разговора, чтобы совершенно очаровать новых знакомых, произвести на них неизгладимое впечатление.']


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    if call.data == 'zodiac':
        answer = random.choice(a) + ' ' + random.choice(b) + ' ' + random.choice(c)
        bot.send_message(call.message.chat.id, answer)


bot.polling(none_stop=True, interval=0)
