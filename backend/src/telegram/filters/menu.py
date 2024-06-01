from aiogram import Bot
from aiogram.types import BotCommand

from diplom_kartigo.backend.src.telegram.filters.lexicon import menu_commands
from diplom_kartigo.config import settings

bot = Bot(token=settings.TOKEN, parse_mode='HTML')

# Кнопка меню, которая упаравляет основным функционалом
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in menu_commands.items()
    ]
    await bot.set_my_commands(main_menu_commands)