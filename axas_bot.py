#!/usr/bin/env python
import telebot
from telebot import types
from telebot.types import Message

TOKEN = '737334966:AAEetwAqs6cq_9ZNbeEBHpyYsDUJ1KXyA_4'
STICKER_ID = 'CAADBQADzwMAAukKyAPJ6kGu2BGu0gI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    # инлайнклавиатура для бота
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Подробнее о нас", url="http://axas-soft.ru")
    keyboard.add(url_button)
    # клавиатура для бота
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Мобильные приложения', 'Веб-платформы')
    keyboard.row('Нейросети', 'Связаться с нами')
    bot.send_message(message.chat.id, '''<b>Добро пожаловать!</b> 
Это телеграм бот компании AXAS. Что Вас интересует?''', reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def contacts_handler(message: Message):
    keyboard = types.InlineKeyboardMarkup()
    if ('Связаться с нами' in message.text):
        site_button = types.InlineKeyboardButton(text="Вебсайт", url="http://axas-soft.ru/")
        vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/axas_soft")
        inst_button = types.InlineKeyboardButton(text="Инстаграм", url="http://axas-soft.ru/")
        fb_button = types.InlineKeyboardButton(text="Фейсбук", url="https://www.facebook.com/iAXAS/")
        keyboard.add(site_button)
        keyboard.add(vk_button)
        keyboard.add(fb_button)
        keyboard.add(inst_button)
        bot.send_message(message.chat.id, "Hаши контакты.", reply_markup=keyboard)
    elif ('Мобильные приложения' in message.text):
        button_1 = types.InlineKeyboardButton(text='Приложение для бизнеса', url="http://axas-soft.ru")
        button_2 = types.InlineKeyboardButton(text='Игры', url="http://axas-soft.ru")
        keyboard.add(button_1, button_2)
        bot.send_message(message.chat.id, 'Какую категорию приложения вы хотите заказать', reply_markup=keyboard)
    elif ('Нейросети' in message.text):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.row(button_phone)
        bot.send_message(message.chat.id, "Оставьте совой номер телефона!", reply_markup=keyboard)
    elif ('Веб-платформы' in message.text):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
        keyboard.row(button_phone)
        bot.send_message(message.chat.id, "Оставьте совой номер телефона!", reply_markup=keyboard)



@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_message(message.chat.id, 'А вот тебе стикер!')
    bot.send_sticker(message.chat.id, STICKER_ID)



@bot.message_handler(commands=['app'])
def choose_buttom(message: Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    callback_button = types.KeyboardButton(text='Android-приложение')
    keyboard.row(u'\uD83C\uDD95' + ' Android-приложение', u'\uD83D\uDC6B' + ' iOS-приложение')
    keyboard.row('Обе платформы')
    bot.send_message(message.chat.id, '''<b>Выберите платформу</b>  ''', reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(commands=["phone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.row(button_phone)
    bot.send_message(message.chat.id, "Оставьте совой номер телефона!", reply_markup=keyboard)


bot.polling(timeout=60)
