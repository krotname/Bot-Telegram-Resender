#!/Usr/bin/python
#
# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

whitelist = ["kreout444", "andrey78787", "StanislavVerigin"]


bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте! \n\n Для помощи ввдеите /help\n\n Для заказа пропуска на автомобиль введите его регистранционный номер')


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id, 'Help message😈')

@bot.message_handler(commands=["avto"])
def start(message):
     bot.send_message(message.chat.id, 'Авто зарегистрировано')\

@bot.message_handler(content_types=["text"])
def messages(message):
    x = 0
    while x < len(whitelist):
     if message.from_user.username == whitelist[x]:
        bot.send_message(config.owner, str(message.from_user.username) +': ' + str(message.from_user.first_name) +': ' + str(message.from_user.last_name) +': ' + message.text)
        bot.send_message(message.chat.id, 'Здравствуйте! Ваша Заявка Принята')
     x += 1


if __name__ == '__main__':
    bot.polling(none_stop=True)
