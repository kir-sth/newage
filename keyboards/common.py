import messages

from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def agreement() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.start_handler.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)
