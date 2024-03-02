import messages

from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_questionnaire() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    reply_builder.add(
        types.KeyboardButton(
            text=messages.start_question.answer
        )
    )
    return reply_builder.as_markup(resize_keyboard=True)


def goal_questionnaire() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.goal_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def gender_questionnaire() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.gender_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def preference_questionnaire() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.preference_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)
