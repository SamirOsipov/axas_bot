#!/usr/bin/env python
import random
import telebot
from telebot import types
from telebot.types import Message

TOKEN = '737334966:AAEetwAqs6cq_9ZNbeEBHpyYsDUJ1KXyA_4'
STICKER_ID = 'CAADBQADzwMAAukKyAPJ6kGu2BGu0gI'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'Привет! Это компания AXAS')



@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_message(message.chat.id, 'А вот тебе стикер, чтобы ты не скучал!')
    bot.send_sticker(message.chat.id, STICKER_ID)


@bot.edited_message_handler(content_types=['text'])
@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
    if 'Samir' in message.text:
        bot.reply_to(message, 'Hi, Samirka')
        return

@bot.message_handler(commands=['start'])
def choose_buttom(message: Message):
    keyboard = types.InlineKeyboardMarkup
    but = types.InlineKeyboardButton(text='Android-приложение')


    bot.reply_to(message, str(random.random()))


bot.polling(timeout=60)
