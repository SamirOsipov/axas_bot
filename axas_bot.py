#!/usr/bin/env python
import telebot
from telebot import types
from telebot.types import Message

TOKEN = '737334966:AAEetwAqs6cq_9ZNbeEBHpyYsDUJ1KXyA_4'
STICKER_ID = 'CAADBQADzwMAAukKyAPJ6kGu2BGu0gI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    # клавиатура для бота
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Мобильные приложения', 'Веб-платформы')
    keyboard.row('Нейросети', 'Связаться с нами')
    button_phone = types.KeyboardButton(text="Отправьте номер телефона, для связи с вами", request_contact=True)
    keyboard.row(button_phone)
    bot.send_message(message.chat.id, '''<b>Добро пожаловать!</b> 
Это телеграм бот компании AXAS. Что Вас интересует?''', reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def contacts_handler(message: Message):
    keyboard = types.InlineKeyboardMarkup()
    if 'Связаться с нами' in message.text:
        site_button = types.InlineKeyboardButton(text="Вебсайт", url="http://axas-soft.ru/")
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/axas_soft")
        inst_button = types.InlineKeyboardButton(text="Инстаграм", url="http://axas-soft.ru/")
        fb_button = types.InlineKeyboardButton(text="Фейсбук", url="https://www.facebook.com/iAXAS/")
        keyboard.add(site_button)
        keyboard.add(vk_button)
        keyboard.add(fb_button)
        keyboard.add(inst_button)
        bot.send_message(message.chat.id, "Hаши контакты.", reply_markup=keyboard)
    elif 'Мобильные приложения' in message.text:
        button_1 = types.InlineKeyboardButton(text='Приложение для бизнеса', callback_data='business_app')
        button_2 = types.InlineKeyboardButton(text='Игры', callback_data='games')
        keyboard.add(button_1, button_2)
        bot.send_message(message.chat.id, 'Какую категорию приложения вы хотите заказать', reply_markup=keyboard)
    elif 'Нейросети' in message.text:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.row(button_phone)
        bot.send_message(message.chat.id, "Оставьте совой номер телефона!", reply_markup=keyboard)
    elif 'Веб-платформы' in message.text:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.row(button_phone)
    elif 'Веб-платформы' in message.text:
        button_1 = types.InlineKeyboardButton(text='Лендинг', callback_data='price')
        button_2 = types.InlineKeyboardButton(text='Интернет-магазин', callback_data='price')
        button_3 = types.InlineKeyboardButton(text='Визитка', callback_data='price')
        button_4 = types.InlineKeyboardButton(text='Каталог', callback_data='price')
        keyboard.add(button_1, button_2)
        keyboard.add(button_3, button_4)
        bot.send_message(message.chat.id, "Оставьте совой номер телефона!", reply_markup=keyboard)


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_message(message.chat.id, 'А вот тебе стикер!')
    bot.send_sticker(message.chat.id, STICKER_ID)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    keyboard = types.InlineKeyboardMarkup()
    # TODO: отправить данные на сервер - почта
    if call.data == 'price':
        keyboard = types.InlineKeyboardMarkup()
        button_1 = types.InlineKeyboardButton(text='Лендинг', callback_data='price')
        button_2 = types.InlineKeyboardButton(text='Интернет-магазин', callback_data='price')
        keyboard.add(button_1, button_2)
        bot.send_message(call.message.chat.id, "Цена", reply_markup=keyboard)
    elif call.data == 'business_app':
        ios_button = types.InlineKeyboardButton(text="iOS-приложение", callback_data='ios')
        android_button = types.InlineKeyboardButton(text="Android-приложение", callback_data='android')
        cross_button = types.InlineKeyboardButton(text="Обе платформы", callback_data='cross')
        keyboard.add(ios_button)
        keyboard.add(android_button)
        keyboard.add(cross_button)
        bot.send_message(call.message.chat.id, 'Выбрать платформу', reply_markup=keyboard)
    elif call.data == 'cross':
        ios_button = types.InlineKeyboardButton(text="Да", callback_data='yes')
        android_button = types.InlineKeyboardButton(text="Нет", callback_data='no')
        keyboard.add(ios_button)
        keyboard.add(android_button)
        bot.send_message(call.message.chat.id, 'Есть ли у Вас Тех задание, код, дизайн?', reply_markup=keyboard)


bot.polling(timeout=60)
