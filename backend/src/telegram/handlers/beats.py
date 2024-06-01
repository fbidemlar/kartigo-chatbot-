from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
import os

from diplom_kartigo.backend.src.telegram.bot import bot
from diplom_kartigo.backend.src.db.models.models import Users, Products
from diplom_kartigo.backend.src.telegram.keyboards.inline.inline import get_genres, to_signup, link_sell
from diplom_kartigo.config import settings


async def beats(message: Message):
    try:
        user = Users.get_current(message.from_user.id)
        genre_list = get_genres()
        register = to_signup()

        if user:
            await message.answer(
                "Давай посмотрим что у нас есть..\n"
                "В нашей подборке ест несколько жанров, которые могут тебя заинтересовать!",
                reply_markup=genre_list
            )
        else:
            await message.answer(
                "Кажется, ты не зарегистрирован у нас. Давай быстренько сделаем это кнопке ниже.\n"
                "После регистрации ты точно сможешь использовать меня.", reply_markup=register
            )
    except Exception as e:
        print("beats:", e)
        await message.answer(
            "Кажется, произошла какая-то ошибка, извините, пожалуйста, мы решаем эти проблемы...."
        )


async def get_beats(callback_query: CallbackQuery):
    try:
        genre = callback_query.data.replace('genre:', '')
        directory = settings.GENRE_PATH + genre + '/'
        files = os.listdir(directory)
        markup = link_sell()

        descriptions = Products.get_descriptions(genre)

        await bot.send_message(
            callback_query.message.chat.id,
            text=f"Вы выбрали жанр {genre}!\n"
                 f"Надеюсь, биты ниже тебе понравятся :)"
        )

        for file, description in zip(files, descriptions):
            audio = FSInputFile(path=directory + file)
            await bot.send_audio(
                callback_query.message.chat.id,
                audio=audio,
                caption=description
            )

        await bot.send_message(
            callback_query.message.chat.id,
            text=f"Если тебе и правда понравились биты, ты сможешь приобрести копию любого бита "
                 f"в формате .wav по ссылке ниже!",
            reply_markup=markup
        )
    except Exception as e:
        print(e)
        await bot.send_message(
            callback_query.id,
            text="Кажется, произошла какая-то ошибка, извините, пожалуйста, мы решаем эти проблемы...."
        )