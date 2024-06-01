from aiogram import Bot, Dispatcher
from diplom_kartigo.config import settings


bot = Bot(token=settings.TOKEN, parse_mode='HTML')
dp = Dispatcher()
