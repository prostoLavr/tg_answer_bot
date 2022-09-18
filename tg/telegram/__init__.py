from telebot.async_telebot import AsyncTeleBot
from telebot import apihelper
import asyncio
from loguru import logger

from time import sleep
import os
import requests


apihelper.SESSION_TIME_TO_LIVE = 5 * 6
bot = AsyncTeleBot(os.environ.get('TELEGRAM_TOKEN'))
logger.level('DEBUG')


# This imports must be below creating the bot
from . import answer_by_template


@logger.catch()
def main():
    global bot
    while True:
        try:
            asyncio.run(bot.polling())
        except requests.exceptions.ReadTimeout or requests.exceptions.ConnectionError:
            logger.critical("ERROR CONNECT TO TELEGRAM")
            sleep(3)
            bot = AsyncTeleBot(os.environ.get('TELEGRAM_TOKEN'))


if __name__ == "__main__":
    main()
