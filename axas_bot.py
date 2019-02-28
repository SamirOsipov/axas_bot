#!/usr/bin/env python
import telebot
from telebot import apihelper
from telebot import types
from telebot.types import Message
import requests
# https://t.me/socks?server=207.154.222.103&port=2720&user=smltproxy&pass=smltelega0272
apihelper.proxy = {'https': 'socks5://smltproxy:smltelega0272@207.154.222.103:2720', 'http': 'socks5://smltproxy:smltelega0272@207.154.222.103:2720'}

TOKEN = '737334966:AAEetwAqs6cq_9ZNbeEBHpyYsDUJ1KXyA_4'

STICKER_ID = 'CAADBQADzwMAAukKyAPJ6kGu2BGu0gI'

bot = telebot.TeleBot(TOKEN)

api = 'http://axas.ru/bot/'

# для сбора данных от пользователя
userData = dict(

)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    # клавиатура для бота
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Мобильные приложения', 'Веб-платформы')
    keyboard.row('Нейросети', 'Контакты')

    bot.send_message(message.chat.id, '''<b>Добро пожаловать!</b> 
Это телеграм бот компании AXAS. Что Вас интересует? Для получения подробной информации просто отправьте Ваш номер 
телефона текстовым сообщением и мы Вам перезвоним''', reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def contacts_handler(message: Message):
    keyboard = types.InlineKeyboardMarkup()
    if 'Мобильные приложения' in message.text:
        button_1 = types.InlineKeyboardButton(text='Приложение для бизнеса', callback_data='business_app')
        button_2 = types.InlineKeyboardButton(text='Игры', callback_data='games')
        keyboard.add(button_1)
        keyboard.add(button_2)
        bot.send_message(message.chat.id, 'Какую категорию приложения вы хотите заказать', reply_markup=keyboard)
        # сначала удаляет старые данные
        userData.clear()
        # потом добавляет данные
        userData.update(soft='Мобильные приложения')
    elif 'Нейросети' in message.text:
        button_phone = types.InlineKeyboardButton(text="Обсудить подробно",callback_data='call_axas')
        keyboard.row(button_phone)
        bot.send_message(message.chat.id, '''Сфера применения нейросетей огромна: искусственная сеть необходима в 
экономике, бизнесе, в медицинской отрасли, в сфере робототехники и в системе связи нейронные сети также необходимы.
Используются они сегодня и в области обработки информации. Перечисленные выше сферы – далеко не полный перечень 
областей, где созданные человеком нейросети могут быть очень полезными. Независимые эксперты уверены, что за нейронными 
сетями будущее. 
Поэтому заказать нейросеть сегодня желают многие компании разного профиля.
Наша компания предлагает такую услугу, как разработка нейросетей для любой области применения. 
Так как каждая область применения подразумевает под собой свою архитектуру нейросетей, специалисты нашей компании 
с особым вниманием подходят к работе над каждым новым проектом''', reply_markup=keyboard)
        userData.clear()
        userData.update(soft='Нейросети')
    elif 'Веб-платформы' in message.text:
        button_1 = types.InlineKeyboardButton(text='Лендинг', callback_data='landing')
        button_2 = types.InlineKeyboardButton(text='Интернет-магазин', callback_data='e-shop')
        keyboard.add(button_1)
        keyboard.add(button_2)
        bot.send_message(message.chat.id, "Оставьте совой номер телефона!", reply_markup=keyboard)
        # сначала удаляет старые данные
        userData.clear()
        # потом добавляет данные
        userData.update(soft='Веб-платформы')
    elif 'Контакты' in message.text:
        site_button = types.InlineKeyboardButton(text="Вебсайт", url="http://axas-soft.ru/")
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/axas_soft")
        inst_button = types.InlineKeyboardButton(text="Инстаграм", url="http://axas-soft.ru/")
        fb_button = types.InlineKeyboardButton(text="Фейсбук", url="https://www.facebook.com/iAXAS/")
        phone_btn = types.InlineKeyboardButton(text="Позвонить", callback_data='call_axas')
        keyboard.add(site_button)
        keyboard.add(vk_button)
        keyboard.add(fb_button)
        keyboard.add(inst_button)
        keyboard.add(phone_btn)
        bot.send_message(message.chat.id, "Hаши контакты.", reply_markup=keyboard)
    else:
        print(message.chat.id)
        bot.send_message('408003762', message.text)
        print(message.text)

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_message(message.chat.id, 'А вот тебе стикер!')
    bot.send_sticker(message.chat.id, STICKER_ID)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = types.InlineKeyboardMarkup()
    if call.data == 'landing':
        button_1 = types.InlineKeyboardButton(text='Узнать цену', callback_data='call_axas')
        keyboard.add(button_1)
        bot.send_message(call.message.chat.id, "Для консультации по стоимости услуги, позвоните нам",
                         reply_markup=keyboard)
        userData.update(website_type='Лендинг')
    elif call.data == 'e-shop':
        button_1 = types.InlineKeyboardButton(text='Узнать цену', callback_data='call_axas')
        keyboard.add(button_1)
        bot.send_message(call.message.chat.id, "Для консультации по стоимости услуги, позвоните нам",
                         reply_markup=keyboard)
        userData.update(website_type='Интернет магазин')
        # юзер выбрал 'Приложение для бизнеса'
    elif call.data == 'business_app':
        ios_button = types.InlineKeyboardButton(text="iOS-приложение", callback_data='ios')
        android_button = types.InlineKeyboardButton(text="Android-приложение", callback_data='android')
        cross_button = types.InlineKeyboardButton(text="Обе платформы", callback_data='cross')
        keyboard.add(ios_button)
        keyboard.add(android_button)
        keyboard.add(cross_button)
        bot.send_message(call.message.chat.id, 'Выбрать платформу', reply_markup=keyboard)
        userData.update(category='Приложение для бизнеса')
        # юзер выбрал 'Игра'
    elif call.data == 'games':
        ios_button = types.InlineKeyboardButton(text="iOS-приложение", callback_data='ios')
        android_button = types.InlineKeyboardButton(text="Android-приложение", callback_data='android')
        cross_button = types.InlineKeyboardButton(text="Обе платформы", callback_data='cross')
        keyboard.add(ios_button)
        keyboard.add(android_button)
        keyboard.add(cross_button)
        bot.send_message(call.message.chat.id, 'Выбрать платформу', reply_markup=keyboard)
        userData.update(category='Игра')
        # юзер выбрал только iOS
    elif call.data == 'ios':
        ios_button = types.InlineKeyboardButton(text="Да", callback_data='yes')
        android_button = types.InlineKeyboardButton(text="Нет", callback_data='no')
        keyboard.add(ios_button)
        keyboard.add(android_button)
        bot.send_message(call.message.chat.id, 'Есть ли у Вас Тех задание, код, дизайн?', reply_markup=keyboard)
        userData.update(platform='iOS')
        # юзер выбрал только андроид
    elif call.data == 'android':
        yes_button = types.InlineKeyboardButton(text="Да", callback_data='yes')
        no_button = types.InlineKeyboardButton(text="Нет", callback_data='no')
        keyboard.add(yes_button, no_button)
        bot.send_message(call.message.chat.id, 'Есть ли у Вас Тех задание, код, дизайн?', reply_markup=keyboard)
        userData.update(platform='Android ')
        # усди юзер выбрад обе платформы
    elif call.data == 'cross':
        ios_button = types.InlineKeyboardButton(text="Да", callback_data='yes')
        android_button = types.InlineKeyboardButton(text="Нет", callback_data='no')
        keyboard.add(ios_button)
        keyboard.add(android_button)
        bot.send_message(call.message.chat.id, 'Есть ли у Вас техническое задание?', reply_markup=keyboard)
        userData.update(platform='И Android и iOS')
    elif call.data == 'call_axas':
        # Отправка номера телефона пользователю
        url = api + 'bot.php'

        params = dict(
            param='phone'
        )
        # ответ от сервера
        resp = requests.post(url=url, data=params)

        # парсинг json
        data = resp.json()
        bot.send_message(call.message.chat.id, "Позвоните нам " + data['phone'])
        # ответ да на вопрос есть ли тех задание
    elif call.data == 'yes':
        yes_button = types.InlineKeyboardButton(text="Да, есть", callback_data='call_axas')
        no_button = types.InlineKeyboardButton(text="Нет", callback_data='call_axas')
        keyboard.add(yes_button, no_button)
        userData.update(tech='yes')
        bot.send_message(call.message.chat.id, "Есть ли у Вас дизайн желаемго продукта?", reply_markup=keyboard)
        # ответ нет на вопрос есть ли тех задание
    elif call.data == 'no':
        userData.update(tech='no')

        url = api + 'bot.php'
        resp = requests.post(url=url, data=userData)

        print(resp.json())

        print(userData)
        bot.send_message(call.message.chat.id, "Спасибо за Ваши ответы, мы свяжемся с Вами в ближайшее время")


# запускаем бота на опрос серверов телеграма
if __name__ == '__main__':
     bot.polling(none_stop=True)
