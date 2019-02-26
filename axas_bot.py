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
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_tell = types.KeyboardButton(text='Рассказать о нас')
    keyboard.add(button_tell)
    bot.send_message(message.chat.id, '''<b>Добро пожаловать!</b> 
    
Привет! Это компания AXAS''', reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_message(message.chat.id, 'А вот тебе стикер!')
    bot.send_sticker(message.chat.id, STICKER_ID)


@bot.message_handler(commands=['app'])
def choose_buttom(message: Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(' Android-приложение', ' iOS-приложение')
    keyboard.row('Обе платформы')


    bot.send_message(message.chat.id, '''<b>Выберите платформу</b>  ''', reply_markup=keyboard,parse_mode='HTML')

   


@bot.message_handler(commands=["phone"])
def geophone(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.row(button_phone)
    bot.send_message(message.chat.id, "Оставьте совой номер телефона!", reply_markup=keyboard)


bot.polling(timeout=60)
