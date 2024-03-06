import messages

from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def start_question() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.start_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def goal_question() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.goal_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def gender_question() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.gender_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def preference_question() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.preference_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def uploading_photo() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.uploading_photo.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def final_form() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.final_form.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)


def end_question() -> types.ReplyKeyboardMarkup:
    reply_builder = ReplyKeyboardBuilder()
    for option in messages.end_question.options:
        reply_builder.add(
            types.KeyboardButton(
                text=option
            )
        )
    return reply_builder.as_markup(resize_keyboard=True)
