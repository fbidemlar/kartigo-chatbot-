from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from diplom_kartigo.backend.src.db.db import session
from diplom_kartigo.backend.src.db.models.models import Genres


def to_signup() -> InlineKeyboardMarkup:
    signup_button = InlineKeyboardButton(text="Регистрация", callback_data="/signup")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[signup_button]])

    return keyboard


def get_genres() -> InlineKeyboardMarkup:
    genres = session.query(Genres).all()

    buttons = [[InlineKeyboardButton(text=genre.name, callback_data=f'genre:{genre.name}')] for genre in genres]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard


def link_sell() -> InlineKeyboardMarkup:
    url = ('https://www.beatstars.com/Kartigo?_gl=1*3ulm43*_ga*NzE3MjMxODE3LjE3MTU4Mzc1MDM.'
           '*_ga_EFBBTCG2XY*MTcxNTgzNzUwMy4xLjEuMTcxNTgzNzg4Ni40Ni4wLjA')
    button = InlineKeyboardButton(text='Приобрести', web_app=WebAppInfo(url=url))
    markup = InlineKeyboardMarkup(inline_keyboard=[[button]])

    return markup


def social_links() -> InlineKeyboardMarkup:
    official_site = 'https://kartigo-1e78b.web.app/'
    tg_channel = 'https://t.me/kartigonews'
    instagram = 'https://www.instagram.com/kartigomusic?igsh=MW5sc3o1MW9wNG5zeA=='
    sell_link = ('https://www.beatstars.com/Kartigo?_gl=1*3ulm43*_ga*NzE3MjMxODE3LjE3MTU4Mzc1MDM.'
                 '*_ga_EFBBTCG2XY*MTcxNTgzNzUwMy4xLjEuMTcxNTgzNzg4Ni40Ni4wLjA')

    official_site_btn = InlineKeyboardButton(text='Официальный сайт', web_app=WebAppInfo(url=official_site))
    tg_channel_btn = InlineKeyboardButton(text='Телеграм канал', url=tg_channel)
    instagram_btn = InlineKeyboardButton(text='Instagram автора', url=instagram)
    sell_link_btn = InlineKeyboardButton(text='Приобрести композиции', web_app=WebAppInfo(url=sell_link))

    markup = InlineKeyboardMarkup(inline_keyboard=[[official_site_btn], [instagram_btn],
                                                   [tg_channel_btn], [sell_link_btn]])
    return markup