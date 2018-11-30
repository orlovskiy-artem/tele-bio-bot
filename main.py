import telebot
import constants
import datetime

bot = telebot.TeleBot(constants.token)

upd = bot.get_updates()
print(upd)
last_upd = upd[-1]
message_from_user = last_upd.message
print(message_from_user)

"""now_start = datetime.datetime.now()
now =  datetime.datetime.now()
today = now.day
today_weekday = datetime.datetime.today().weekday()
hour = now.hour"""

@bot.message_handler(commands = ['start'])
def handle_command(message):
    bot.send_message(message.chat.id,"""Добрий день!
Вас вітає бот (тільки для біологів). Я працюю з певними командами. Натисніть "/" для їх перегляду. Приємного Вам користування.
    
(Бот знаходиться на стадії розробки. Всю конструтивну критику та побажання писати розробнику бота.""")
    print("Command start")

@bot.message_handler(commands = ['help'])
def handle_command(message):
    bot.send_message(message.chat.id,"Вам не потрібна допомога. Нє, ну а що тут складного? :)")
    bot.send_sticker(message.chat.id,"CAADAgADVAADKOeIDbibiciztv3RAg")
    print("Command help")

@bot.message_handler(commands = ['today'])
def handle_command(message):
    print("command today")
    today = datetime.datetime.now().day
    month_now = datetime.datetime.now().month
    year_now = datetime.datetime.now().year

    if(today == 3 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Понеділок (03.12)
    Група баби всі кр.
    Залік з укр мови (заліковки)""")

    elif(today == 4 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Вівторок (04.12)
    10:35 модуль з ботаніки + альбом(2 гр)
    14:00 вступ залік 34 ауд. ММФ""")

    elif(today == 5 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Середа (05.12)
    Група мужика: тести
    10:00 модуль з ботаніки (1 гр)""")

    elif(today == 6 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Четвер (06.12)
    10:35 модуль екологія
    14:05 модуль цитологія (2 гр)""")

    elif(today == 7 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""П'ятниця (07.12)
    12:20 модуль цитологія (1 гр)""")

    else:
        bot.send_message(message.chat.id,"""Поки шикуєм""")

@bot.message_handler(commands = ['tommorow'])
def handle_command(message):
    print("command tommorow")
    today = datetime.datetime.now().day
    month_now = datetime.datetime.now().month
    year_now = datetime.datetime.now().year

    if(today == 2 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Понеділок (03.12)
    Група баби всі кр.
    Залік з укр мови (заліковки)""")

    elif(today == 3 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Вівторок (04.12)
    10:35 модуль з ботаніки + альбом(2 гр)
    14:00 вступ залік 34 ауд. ММФ""")

    elif(today == 4 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Середа (05.12)
    Група мужика: тести
    10:00 модуль з ботаніки (1 гр)""")

    elif(today == 5 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""Четвер (06.12)
    10:35 модуль екологія
    14:05 модуль цитологія (2 гр)""")

    elif(today == 6 and month_now == 12 and year_now==2018):
        bot.send_message(message.chat.id,"""П'ятниця (07.12)
    12:20 модуль цитологія (1 гр)""")

    else:
        bot.send_message(message.chat.id,"""Поки шикуєм""")

@bot.message_handler(commands = ['week'])
def handle_command(message):
    print("command week")
    week_number = datetime.date.today().isocalendar()[1] # weekNumber (isocalendar()[1] 1 - means week number)
    if(week_number==49):
        bot.send_message(message.chat.id,
    """Понеділок (03.12)
    Група баби всі кр.
    Залік з укр мови (заліковки)
    
Вівторок (04.12)
    10:35 модуль з ботаніки + альбом(2 гр)
    14:00 вступ залік 34 ауд. ММФ

Середа (05.12)
    Група мужика: тести
    10:00 модуль з ботаніки (1 гр)
    
Четвер (06.12)
    10:35 модуль екологія
    14:05 модуль цитологія (2 гр)
    
П'ятниця (07.12)
    12:20 модуль цитологія (1 гр)
 """)
    else:
        bot.send_message(message.chat.id,"""Поки шикуєм""")



@bot.message_handler(commands = ['nextweek'])
def handle_command(message):
    print("command nextweek")
    week_number = datetime.date.today().isocalendar()[1] # weekNumber (isocalendar()[1] 1 - means week number)
    if(week_number==48):
        bot.send_message(message.chat.id,
    """Понеділок (03.12)
    Група баби всі кр.
    Залік з укр мови (заліковки)
    
Вівторок (04.12)
    10:35 модуль з ботаніки + альбом(2 гр)
    14:00 вступ залік 34 ауд. ММФ

Середа (05.12)
    Група мужика: тести
    10:00 модуль з ботаніки (1 гр)
    
Четвер (06.12)
    10:35 модуль екологія
    14:05 модуль цитологія (2 гр)
    
П'ятниця (07.12)
    12:20 модуль цитологія (1 гр)
 """)
    else:
        bot.send_message(message.chat.id,"""Поки шикуєм""")


@bot.message_handler(commands = ['timetable'])
def handle_command(message):
    print("command timetable")
    bot.send_message(message.chat.id,"""1 пара 8:40 - 10:15
2 пара 10:35 - 12:10
3 пара 12:20 - 13:55
4 пара 14:05 - 15:40""")

@bot.message_handler(commands = ['left'])
def handle_command(message):
    print("command left")
    now =  datetime.datetime.now()
    hour = now.hour+2
    time_abs_sec = hour*7200 + now.minute*60 + now.second

    # First lesson
    if(time_abs_sec>=8*7200+40*60 and time_abs_sec<=10*7200+15*60):
        delta = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,
                             datetime.datetime.now().day,10,15,0,0) - datetime.datetime.today()
        delta = delta.seconds - 7200
        hours = str(delta//3600)
        minutes = str((delta - int(hours)*3600)//60)
        seconds = str(delta - 3600*int(hours)-60*int(minutes))
        bot.send_message(message.chat.id,"Залишилось " + hours + " годин " + minutes + " хвилин " +  seconds + " секунд")

    #Second lesson
    elif(time_abs_sec>=10*7200+35*60 and time_abs_sec<=12*7200+10*60):
        delta = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,
                             datetime.datetime.now().day,12,10,0,0) - datetime.datetime.today()
        delta = delta.seconds - 7200
        hours = str(delta//3600)
        minutes = str((delta - int(hours)*3600)//60)
        seconds = str(delta - 3600*int(hours)-60*int(minutes))
        bot.send_message(message.chat.id,"Залишилось " + hours + " годин " + minutes + " хвилин " +  seconds + " секунд")

    #Third lesson
    elif(time_abs_sec>=12*7200+20*60 and time_abs_sec<=13*7200+55*60):
        delta = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,
                             datetime.datetime.now().day,13,55,0,0) - datetime.datetime.today()
        delta = delta.seconds - 7200
        hours = str(delta//3600)
        minutes = str((delta - int(hours)*3600)//60)
        seconds = str(delta - 3600*int(hours)-60*int(minutes))
        bot.send_message(message.chat.id,"Залишилось " + hours + " годин " + minutes + " хвилин " +  seconds + " секунд")

    #Fourth lesson
    elif(time_abs_sec>=14*7200+5*60 and time_abs_sec<=15*7200+40*60):
        delta = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,
                             datetime.datetime.now().day,15,40,0,0) - datetime.datetime.today()
        delta = delta.seconds - 7200
        hours = str(delta//3600)
        minutes = str((delta - int(hours)*3600)//60)
        seconds = str(delta - 3600*int(hours)-60*int(minutes))
        bot.send_message(message.chat.id,"Залишилось " + hours + " годин " + minutes + " хвилин " +  seconds + " секунд")

    #No lesson
    else:
        bot.send_message(message.chat.id,"Зараз немає пар")

    """delta =datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,
                             datetime.datetime.now().day,18,0,0,0) - datetime.datetime.today()
    delta = delta.seconds - 7200
    hours = str(delta//3600)
    minutes = str((delta - int(hours)*3600)//60)
    seconds = str(delta - 3600*int(hours)-60*int(minutes))

    bot.send_message(message.chat.id,"Тест на 18 год. Залишилось " + hours + " годин " + minutes + " хвилин " +  seconds + " секунд")
    """


"""
@bot.message_handler(content_types=['text'])
def handle_text(message):
    now =  datetime.datetime.now()
    today = now.day
    today_weekday = datetime.datetime.today().weekday()
    hour = now.hour
    if message.text == "Windows":
        bot.send_message(chat_id=message.chat.id,text="*Linux*",parse_mode=telegram.ParseMode.MARKDOWN)
    print("Пришел текст")
"""

@bot.message_handler(content_types=['sticker'])
def upd(message):
    now =  datetime.datetime.now()
    today = now.day
    today_weekday = datetime.datetime.today().weekday()
    hour = now.hour
    upd = bot.get_updates()
    print(upd)
    last_upd = upd[-1]
    print(last_upd)

"""@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
"""
"""
@bot.message_handler(content_types=['text'])
def upd(message):
   print(upd)

@bot.message_handler(commands = ['nextweek,week,start,help,today,help'])
def upd(message):
   print(upd)
"""
while(True):
    try:
        if __name__ == "__main__":
            bot.polling(none_stop=True,interval=0)
    except:
        pass


"""if(week_number%2==1):
        if today_weekday == 0:
            bot.send_message(message.chat.id,
        ""Понеділок
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Іноземна мова, ауд. 602, 603 ММФ
    3) Екологія (сем), ауд. 602 ММФ
    4) Хімія (пр), 2 підгрупа, ауд. 31 лаб. корп. БФ"")

        if today_weekday == 1:
            bot.send_message(message.chat.id,""Вівторок
    1) Хімія (пр), 1 підгрупа, ауд. 31 лаб. корп. БФ
    
    3) Хімія (лек), ауд. 610 ММФ"")

        if today_weekday == 2:
            bot.send_message(message.chat.id,""Середа
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Українська мова (пр), ауд. 602 ММФ
    3) Хімія (лек)
    4) Ботаніка (лаб), група 2, ауд. 404 БФ"")

        if today_weekday == 3:
            bot.send_message(message.chat.id,""Четвер
    1) Вступ до університетських студій
    2) Екологія (лек), ауд. 212 БФ
    3) Ботаніка (лек), ауд. 411 БФ
    4) Ботаніка (лаб), група 1, ауд. 404 БФ"")

        if today_weekday == 4:
            bot.send_message(message.chat.id,""П'ятниця
    2) Логіка (лек), 602 ММФ
    3) Цитологія (лаб), група 1, ауд. 517 БФ
    4) Хімія лаб корпус ННЦ, ауд. 31
 "")

        if today_weekday>4:
            bot.send_message(message.chat.id,""
        Радуйся! Сьогодні пар немає)
        "")
            bot.send_sticker(message.chat.id,"CAADAgADUwADKOeIDc1_Adm2zv4cAg")

    else:
        if today_weekday == 0:
            bot.send_message(message.chat.id,
        ""Понеділок
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Іноземна мова, ауд. 602, 603 ММФ
    3) Українська мова (лек), з 24.09.18, ауд. 602 ММФ
    4) Хімія лаб корпус ННЦ, ауд. 31"")

        if today_weekday == 1:
            bot.send_message(message.chat.id,""Вівторок
    1) Хімія (пр), 1 підгрупа, ауд. 31 лаб. корп. БФ
    
    3) Хімія (лек), ауд. 610 ММФ"")

        if today_weekday == 2:
            bot.send_message(message.chat.id,""Середа
    1) Іноземна мова, ауд. 602, 603 ММФ
    2) Українська мова (пр), ауд. 602 ММФ
    3) Хімія (лек)
    4) Хімія лаб корпус ННЦ, ауд. 31"")

        if today_weekday == 3:
            bot.send_message(message.chat.id,""Четвер
    1) Вступ до університетських студій
    2) Екологія (лек), ауд. 212 БФ
    3) Ботаніка (лек), ауд. 411 БФ
    4) Цитологія (лаб), група 2, ауд. 517 БФ"")

        if today_weekday == 4:
            bot.send_message(message.chat.id,""П'ятниця
    1) Логіка (лек), ауд. 602 ММФ
    2) Логіка (лек), 602 ММФ
    3) Цитологія (лаб), група 1, ауд. 517 БФ
    4) Хімія лаб корпус ННЦ, ауд. 31
 "")

        if today_weekday>4:
            bot.send_message(message.chat.id,""
        Радуйся! Сьогодні пар немає)
        "")
            bot.send_sticker(message.chat.id,"CAADAgADUwADKOeIDc1_Adm2zv4cAg")"""
#today_weekday = datetime.datetime.today().weekday()
#week_number = datetime.date.today().isocalendar()[1]
