from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def agreement() -> types.InlineKeyboardMarkup:
    inline_builder = InlineKeyboardBuilder()
    inline_builder.add(
        types.InlineKeyboardButton(
            text="cогласен",
            callback_data="agreement"
        )
    )
    inline_builder.add(
        types.InlineKeyboardButton(
            text="не согласен",
            callback_data="disagreement"
        )
    )
    return inline_builder.as_markup()
