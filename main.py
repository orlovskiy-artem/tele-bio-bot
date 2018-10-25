import flask
import telebot
import constants
import datetime

bot = telebot.TeleBot(constants.token)

upd = bot.get_updates()
print(upd)
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

now = datetime.datetime.now()
today = now.day
today_weekday = datetime.datetime.today().weekday()
hour = now.hour

@bot.message_handler(commands = ['start'])
def handle_command(message):
    bot.send_message(message.chat.id,"""Добрий день!
Вас вітає бот (тільки для біологів). Я супер продвинутий. Майже штучний інтелект. Тільки думати я не вмію, а так нічого. Я працюю з певними командами. Натисніть "/" для їх перегляду. Приємного вам користування.
    
(Бот знаходиться на стадії розробки. Будь-яке хейтерство, плювання в сторону бота і крики "Який ідіот це кодив?" не є можливими.
Всю конструтивну критику та побажання писати розробнику бота)""")
    print("Пришла Комманда")

@bot.message_handler(commands = ['help'])
def handle_command(message):
    bot.send_message(message.chat.id,"Вам не потрібна допомога. Нє, ну а що тут складного? :)")


@bot.message_handler(commands = ['today'])
def handle_command(message):
    if today_weekday == 0:
        bot.send_message(message.chat.id,
        """Понеділок
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Іноземна мова, ауд. 602, 603 ММФ
    3) Екологія (сем), ауд. 602 ММФ/Українська мова (лек), з 24.09.18, ауд. 602 ММФ
    4) Хімія (пр), 2 підгрупа, ауд. 31 лаб. корп. БФ/Хімія лаб корпус ННЦ, ауд. 31""")
    if today_weekday == 1:
        bot.send_message(message.chat.id,"""Вівторок
    1) Хімія (пр), 1 підгрупа, ауд. 31 лаб. корп. БФ
    2) 
    3) Хімія (лек), ауд. 610 ММФ""")

    if today_weekday == 2:
        bot.send_message(message.chat.id,"""Середа
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Українська мова (пр), ауд. 602 ММФ
    3) Хімія (лек)
    4) Ботаніка (лаб), група 2, ауд. 404 БФ/хімія лаб корпус ННЦ, ауд. 31""")

    if today_weekday == 3:
        bot.send_message(message.chat.id,"""Четвер
    1) Вступ до унфверситетських студій
    2) Екологія (лек), ауд. 212 БФ
    3) Ботаніка (лек), ауд. 411 БФ
    4) Ботаніка (лаб), група 1, ауд. 404 БФ Цитологія (лаб), група 2, ауд. 517 БФ""")

    if today_weekday == 4:
        bot.send_message(message.chat.id,"""П'ятниця
    (2 Тиждень) 1)Логіка (лек), ауд. 602 ММФ
    2) Логіка (лек), 602 ММФ
    3) Цитологія (лаб), група 1, ауд. 517 БФ
    4) Хімія лаб корпус ННЦ, ауд. 31
 """)
    if today_weekday>4:
        bot.send_message(message.chat.id,"""
        Радуйся! Сьогодні пар немає)
        """
 )

@bot.message_handler(commands = ['tommorow'])
def handle_command(message):
    if today_weekday == 0:
        bot.send_message(message.chat.id,
        """Вівторок
    1) Хімія (пр), 1 підгрупа, ауд. 31 лаб. корп. БФ
    2) 
    3) Хімія (лек), ауд. 610 ММФ""")

    if today_weekday == 1:
        bot.send_message(message.chat.id,"""Середа
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Українська мова (пр), ауд. 602 ММФ
    3) Хімія (лек)
    4) Ботаніка (лаб), група 2, ауд. 404 БФ""")

    if today_weekday == 2:
        bot.send_message(message.chat.id,"""Четвер
    2) Екологія (лек), ауд. 212 БФ
    3) Ботаніка (лек), ауд. 411 БФ
    4) Ботаніка (лаб), група 1, ауд. 404 БФ Цитологія (лаб), група 2, ауд. 517 БФ""")

    if today_weekday == 3:
        bot.send_message(message.chat.id,"""П'ятниця
    2 Тиждень 1)    
    2) Логіка (лек), 602 ММФ
    3) Цитологія (лаб), група 1, ауд. 517 БФ""")

@bot.message_handler(commands = ['week'])
def handle_command(message):
    bot.send_message(message.chat.id,
    """Понеділок
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Іноземна мова, ауд. 602, 603 ММФ
    3) Екологія (сем), ауд. 602 ММФ/Українська мова (лек), з 24.09.18, ауд. 602 ММФ
    4) Хімія (пр), 2 підгрупа, ауд. 31 лаб. корп. БФ/Хімія лаб корпус ННЦ, ауд. 31
    
Вівторок
    1) Хімія (пр), 1 підгрупа, ауд. 31 лаб. корп. БФ
    2) Цитологія (лек), ауд. 212 БФ
    3) Хімія (лек), ауд. 610 ММФ
    4) Вступ до університетських студій

Середа
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Українська мова (пр), ауд. 602 ММФ
    3) Хімія (лек)
    4) Ботаніка (лаб), група 2, ауд. 404 БФ

Четвер
    2) Екологія (лек), ауд. 212 БФ
    3) Ботаніка (лек), ауд. 411 БФ
    4) Ботаніка (лаб), група 1, ауд. 404 БФ Цитологія (лаб), група 2, ауд. 517 БФ
    
П'ятниця
    (2 Тиждень) 1)Логіка (лек), ауд. 602 ММФ
    2) Логіка (лек), 602 ММФ
    3) Цитологія (лаб), група 1, ауд. 517 БФ

 """)

@bot.message_handler(commands = ['nextweek'])
def handle_command(message):
    bot.send_message(message.chat.id,
    """Понеділок
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Іноземна мова, ауд. 602, 603 ММФ
    3) Екологія (сем), ауд. 602 ММФ
    4) Хімія (пр), 2 підгрупа, ауд. 31 лаб. корп. БФ/Хімія лаб корпус ННЦ, ауд. 31
    
Вівторок
    1) Хімія (пр), 1 підгрупа, ауд. 31 лаб. корп. БФ
    2) Цитологія (лек), ауд. 212 БФ
    3) Хімія (лек), ауд. 610 ММФ
    4) Вступ до університетських студій

Середа
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Українська мова (пр), ауд. 602 ММФ
    3) Хімія (лек)
    4) Ботаніка (лаб), група 2, ауд. 404 БФ

Четвер
    2) Екологія (лек), ауд. 212 БФ
    3) Ботаніка (лек), ауд. 411 БФ
    4) Ботаніка (лаб), група 1, ауд. 404 БФ Цитологія (лаб), група 2, ауд. 517 БФ
    
П'ятниця
    (2 Тиждень) 1)Логіка (лек), ауд. 602 ММФ
    2) Логіка (лек), 602 ММФ
    3) Цитологія (лаб), група 1, ауд. 517 БФ

 """)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "Windows":
        bot.send_message(message.chat.id,"Linux")
    print("Пришел текст")

"""@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
"""

@bot.message_handler(content_types=['sticker'])
def upd(message):
   print(last_upd)


"""
@bot.message_handler(content_types=['text'])
def upd(message):
   print(upd)

@bot.message_handler(commands = ['nextweek,week,start,help,today,help'])
def upd(message):
   print(upd)
"""
if __name__ == "__main__":
    bot.polling(none_stop=True,interval=0)
