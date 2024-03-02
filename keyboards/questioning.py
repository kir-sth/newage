from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_questionnaire() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    reply_builder.add(
        types.KeyboardButton(
            text="Заполнить анкету!"
        )
    )
    return reply_builder.as_markup(resize_keyboard=True)
