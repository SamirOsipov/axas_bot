#!/usr/bin/env python
import telebot
from telebot import types
from telebot.types import Message

TOKEN = '737334966:AAEetwAqs6cq_9ZNbeEBHpyYsDUJ1KXyA_4'
STICKER_ID = 'CAADBQADzwMAAukKyAPJ6kGu2BGu0gI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    #клавиатура для бота
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Мобильные приложения', 'Веб-платформы')
    keyboard.row('Нейросети', 'Связаться с нами')
    bot.send_message(message.chat.id, '''<b>Добро пожаловать!</b> 
    Это телеграм бот компании AXAS. Что Вас интересует?''', reply_markup=keyboard, parse_mode='HTML')

@bot.message_handler(commands=['contacts'])
def default_test(message):
    keyboard = types.InlineKeyboardMarkup()
    site_button = types.InlineKeyboardButton(text="Вебсайт", url="http://axas-soft.ru/")
    vk_button = types.InlineKeyboardButton(text="Вконтакте", url="https://vk.com/axas_soft")
    inst_button = types.InlineKeyboardButton(text="Инстаграм", url="http://axas-soft.ru/")
    fb_button = types.InlineKeyboardButton(text="Фейсбук", url="https://www.facebook.com/iAXAS/")
    keyboard.add(site_button)
    keyboard.add(vk_button)
    keyboard.add(fb_button)
    keyboard.add(inst_button)
    bot.send_message(message.chat.id, "Hаши контакты.", reply_markup=keyboard)


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_message(message.chat.id, 'А вот тебе стикер!')
    bot.send_sticker(message.chat.id, STICKER_ID)


@bot.message_handler(commands=['app'])
def choose_buttom(message: Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Android-приложение', ' iOS-приложение')
    keyboard.row('Обе платформы')


    bot.send_message(message.chat.id, '''<b>Выберите платформу</b>  ''', reply_markup=keyboard, parse_mode='HTML')

   



bot.polling(timeout=60)
