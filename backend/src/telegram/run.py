from aiogram.filters import Command, CommandStart


from diplom_kartigo.backend.src.db.db import Base, engine
from diplom_kartigo.backend.src.telegram.bot import bot, dp

from diplom_kartigo.backend.src.telegram.handlers.start import start
from diplom_kartigo.backend.src.telegram.handlers.signup import signup, get_phone
from diplom_kartigo.backend.src.telegram.handlers.beats import beats, get_beats
from diplom_kartigo.backend.src.telegram.handlers.about import about
from diplom_kartigo.backend.src.telegram.handlers.social import social
from diplom_kartigo.backend.src.telegram.filters.menu import set_main_menu
from diplom_kartigo.backend.src.telegram.states import States


if __name__ == '__main__':
    # Инициализация базы данных
    Base.metadata.create_all(bind=engine)
    print("База инициализирована")
    # Регистрация кнопки меню в чате
    dp.startup.register(set_main_menu)

    # Регистрация команды /start
    dp.message.register(start, CommandStart())

    # Регистрация команды /signup
    dp.callback_query.register(signup, lambda c: c.data == '/signup')
    dp.message.register(get_phone, States.phone)

    # Регистрация команды /beats
    dp.message.register(beats, Command('beats'))
    dp.callback_query.register(get_beats, lambda c: c.data.startswith('genre'))

    # Регистрация команды /about
    dp.message.register(about, Command('about'))

    # Регистрация команды /social
    dp.message.register(social, Command('social'))

    print("Бот запущен")
    dp.run_polling(bot)