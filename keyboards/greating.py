from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def lets_start() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    reply_builder.add(
        types.KeyboardButton(
            text="давай начнем"
        )
    )
    return reply_builder.as_markup(resize_keyboard=True)


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
