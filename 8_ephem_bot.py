"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import pendulum
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {'proxy_url': settings.PROXY_URL, 'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME,
         'password': settings.PROXY_PASSWORD}}


def greet_user(update, context):
    user_text = update.message.text
    if 'start' in user_text:
        user_text = 'Вызван /start'
    else:
        user_text = 'Вызван /planet'
    print(user_text)
    update.message.reply_text('Введите название планеты\n(на русском языке)')


def talk_to_me(update, context):
    planet_name = update.message.text
    planet_name = planet_name.capitalize()
    print(planet_name)
    tomorrow = pendulum.tomorrow('Europe/Moscow').format('DD.MM')
    if 'Меркурий' in planet_name:
        planet_name = ephem.Mercury(tomorrow)
        constellation = ephem.constellation(planet_name)
    elif 'Венера' in planet_name:
        planet_name = ephem.Venus(tomorrow)
        constellation = ephem.constellation(planet_name)
    elif 'Земля' in planet_name:
        planet_name = ephem.Earth(tomorrow)
        constellation = ephem.constellation(planet_name)
    elif 'Марс' in planet_name:
        planet_name = ephem.Mars(tomorrow)
        constellation = ephem.constellation(planet_name)
    elif 'Юпитер' in planet_name:
        planet_name = ephem.Jupiter(tomorrow)
        constellation = ephem.constellation(planet_name)
    elif 'Сатурн' in planet_name:
        planet_name = ephem.Saturn(tomorrow)
        constellation = ephem.constellation(planet_name)
    elif 'Уран' in planet_name:
        planet_name = ephem.Uranus(tomorrow)
        constellation = ephem.constellation(planet_name)
    elif 'Нептун' in planet_name:
        planet_name = ephem.Neptune(tomorrow)
        constellation = ephem.constellation(planet_name)
    print(constellation)
    update.message.reply_text(constellation)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
