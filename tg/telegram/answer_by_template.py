import telebot
from loguru import logger
from random import randint

from . import bot


def clean_key(key: str, is_bot: bool = False) -> tuple[str]:
    for i in ('?', '!', ',', '.', '(', ')'):
        key = key.replace(i, ' ')
    key = key.lower().strip()
    if not is_bot:
        if is_enjoy(key):
            return ('{смех}',)
        parts = [key_part for key_part in key.split() if not is_enjoy(key_part)]
    else:
        parts = key.split()
    return tuple(sorted(parts))


def is_enjoy(word: str):
    return not any(letter not in 'авх' for letter in word)

with open('./answers.txt') as file:
    answers = {} 
    lines = [line.strip().replace('  ', ' ').split(' = ') 
             for line in file.readlines()]
    for keys, values in lines:
        values = values.split(' - ')
        for key in keys.split(' - '):
            key = clean_key(key, is_bot=True)
            answers[key] = values
    logger.info(f'Answers: {answers}')

@bot.message_handler(func=lambda msg: True)
async def start(message: telebot.types.Message):
    logger.debug(f'Get message: {message.text}')
    key = clean_key(message.text)
    logger.debug(f'Clean key: {key}')
    values = (answers.get(key) or
              answers[ ('*',) ])
    answer = values[randint(0, len(values) - 1)] 
    await bot.send_message(message.from_user.id, answer)

