from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.media_group import MediaGroupBuilder
from typing import Any, Dict, List

from .utls import get_years_old


class Question():
    def __init__(self, text):
        self.text = text


class ClosedQuestion(Question):
    def __init__(self, text, options):
        super().__init__(text)
        self.options = options

    def get_keyboard(self) -> types.ReplyKeyboardMarkup:
        reply_builder = ReplyKeyboardBuilder()
        for option in self.options:
            reply_builder.add(
                types.KeyboardButton(
                    text=option
                )
            )
        return reply_builder.as_markup(resize_keyboard=True)


class UploadingPhoto(ClosedQuestion):
    def __init__(self, text, first, second, third, options):
        super().__init__(text, options)
        self.first = first
        self.second = second
        self.third = third


class FinalForm(ClosedQuestion):
    def __init__(self, text, options):
        super().__init__(text, options)

    def form_builder(self, user_data: Dict[str, Any]) -> List[types.InputMediaPhoto]:
        name = user_data["name"]
        age = user_data["age"]
        years_old = get_years_old(age)
        description = user_data["description"]
        album_builder = MediaGroupBuilder(
            caption=f"{name}, {age} {years_old}, город\n{description}"
        )
        if "first_photo" in user_data:
            album_builder.add_photo(
                media=user_data["first_photo"]
            )
        if "second_photo" in user_data:
            album_builder.add_photo(
                media=user_data["second_photo"]
            )
        if "third_photo" in user_data:
            album_builder.add_photo(
                media=user_data["third_photo"]
            )
        return album_builder.build()

