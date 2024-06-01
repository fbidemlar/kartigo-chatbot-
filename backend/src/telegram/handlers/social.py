from aiogram.types import Message
from diplom_kartigo.backend.src.telegram.keyboards.inline.inline import social_links

async def social(message: Message):
    try:
        markup = social_links()
        await message.answer(
            "Кажется, ты хочешь узнать больше об авторе :)\n"
            "Переходи по ссылкам ниже и сможешь узнать больше, "
            "также по ссылке внизу ты сможешь приобрести понравившиеся композиции", reply_markup=markup
        )
    except Exception as e:
        print('about:', e)
        await message.answer(
            "Кажется, произошла какая-то ошибка, извините, пожалуйста, мы решаем эти проблемы...."
        )