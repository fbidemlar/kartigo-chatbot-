from aiogram.types import Message
from diplom_kartigo.backend.src.db.models.models import Users
from diplom_kartigo.backend.src.telegram.keyboards.inline.inline import to_signup

async def start(message: Message):
    try:
        user = Users.get_current(message.from_user.id)

        signup_user = to_signup()

        if user:
            await message.answer(
                "Привет! Рады, что Вы вернулись к нам!\n"
                "Хотите послушать авторские биты от @kartigo или почитать свежие новости? "
                "Тогда давай посмотрим Меню"
            )
        else:
            await message.answer(
                "Добро пожаловать в нашу команду!\n"
                "Тут ты сможешь приобрести авторский биты от @kartigo, "
                "узнать последние новости музыкальной индустрии и многое другое.\n"
                "\n"
                "Но перед этим, давай сначала зарегистрируем тебя по кнопке ниже", reply_markup=signup_user
            )
    except Exception as e:
        print("start:", e)
        await message.answer(
            "Кажется, произошла какая-то ошибка, извините, пожалуйста, мы решаем эти проблемы...."
        )