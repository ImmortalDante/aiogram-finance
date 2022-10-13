from aiogram import Bot
from aiogram.dispatcher import Dispatcher

import config


bot = Bot(config.SECRET_KEY)
dp = Dispatcher(bot)
