#!/Usr/bin/python
#
# -*- coding: utf-8 -*-
import os
import sys

import telebot

import config

print("\nsuccess restarted")

restart = input("\nDo you want to restart the BOT? > ")

if restart:

    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

else:
    print("\nThe programm will be manual restarted")

whitelist = open('C:\\bot\\whitelist.csv', "r+").read().splitlines()

group1 = -1001480216119

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
                     'Здравствуйте! \n\nДля заказа пропуска на автомобиль в подземный паркинг отправьте заявку в '
                     'формате: \n\n🏢 Башня для разгрузки\n⏰ Дата и время въезда\n🚘 Марка автомобиля\n🆔 Гос. номер '
                     'автомобиля\n\nДля помощи введите /help')


@bot.message_handler(commands=["help"])
def start(message):
    bot.send_message(message.chat.id,
                     'В случае возникновения проблем при заказе пропуска- обратитесь к администратору Вашей башни в '
                     'холле первого этажа.👨')


@bot.message_handler(commands=["avto"])
def start(message):
    bot.send_message(message.chat.id, 'Авто зарегистрировано') \
 \
    @ bot.message_handler(content_types=["text"])

    def messages(message):
        x = 0
        while x < len(whitelist):
            if message.from_user.username == whitelist[x]:
                bot.send_message(group1,
                                 str(message.from_user.username) + ': ' + str(
                                     message.from_user.first_name) + ': ' + str(
                                     message.from_user.last_name) + ': ' + message.text)
                bot.send_message(message.chat.id, 'Здравствуйте! Ваша Заявка Принята')
            x += 1


if __name__ == '__main__':
    bot.polling(none_stop=True)
