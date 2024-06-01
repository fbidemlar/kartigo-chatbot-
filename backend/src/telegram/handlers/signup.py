from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from diplom_kartigo.backend.src.telegram.bot import bot
from diplom_kartigo.backend.src.db.models.models import Users
from diplom_kartigo.backend.src.telegram.states import States


async def signup(callback_query: CallbackQuery, state: FSMContext):
    try:
        user = Users.get_current(callback_query.from_user.id)

        if user:
            await bot.send_message(
                callback_query.from_user.id,
                "Ты, оказывается, зарегистрирован у нас!\n"
                "Хотите послушать авторские биты от @kartigo или почитать свежие новости? "
                "Тогда давай посмотрим Меню"
            )
        else:
            await bot.send_message(
                callback_query.from_user.id,
                "Так... Зарегистрируем тебя...\n"
                "Напиши свой номер телефона в следующем сообщении.."
            )
            await state.set_state(States.phone)
    except Exception as e:
        print("start:", e)
        await bot.send_message("Кажется, произошла какая-то ошибка, извините, пожалуйста, мы решаем эти проблемы....")


async def get_phone(message: Message, state: FSMContext):
    try:
        await state.update_data(phone=message.text)

        get_data = await state.get_data()
        phone = get_data.get('phone')

        new_user = Users.create(
            tg_id = message.from_user.id,
            tg_username = message.from_user.username,
            first_name = message.from_user.first_name,
            phone_number = phone
        )
        print(new_user)

        await message.answer(
            f"Хорошо, {message.from_user.first_name}, теперь мы можем продолжить работу!\n"
            f"Теперь ты можешь пользоваться моим меню. Успехов тебе!"
        )
    except Exception as e:
        print("get_phone:", e)
        await message.answer("Кажется, произошла какая-то ошибка, извините, пожалуйста, мы решаем эти проблемы....")
    finally:
        await state.clear()