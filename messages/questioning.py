from .utls import get_years_old

from aiogram import types
from aiogram.utils.media_group import MediaGroupBuilder
from typing import Any, Dict, List


class start_question():
    text = "Отлично! Давай начнем заполнять твою анкету?"
    options = (
        "Давай заполним!",
    )


class goal_question():
    text = "Кого ты хочешь найти?"
    options = (
        "знакомства/друзей",
        "партнера"
    )


class gender_question():
    text = "Теперь определимся с полом"
    options = (
        "Я девушка",
        "Я парень",
        "Не хочу выбирать"
    )


class preference_question():
    text = "Кто тебе интересен?"
    options = (
        "Девушки",
        "Парни",
        "Все"
    )


class name_question():
    text = "Как тебя зовут?"


class age_question():
    text = "Сколько тебе лет?"


class description_question():
    text = "Напиши описание своей анкеты"


class photo_question():
    text = "Приложи 1 фото к своей анкете"


class uploading_photo():
    text = "Поймал твое фото!"
    first = "Ты приложил 1/3 фото. Можешь загрузить еще фото или закончить оформление анкеты"
    second = "Ты приложил 2/3 фото. Можешь загрузить еще фото или закончить оформление анкеты"
    third = "Ты приложил 3/3 фото. Пора закончить оформление анкеты"
    options = (
        "закончить",
    )

class final_form():
    text = "Вот твоя итоговая анкета"

    def form_builder(user_data: Dict[str, Any]) -> List[types.InputMediaPhoto]:
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
    
    options = {
        "отлично!",
    }


class end_question():
    text = "Начнем поиск знакомств!"
    options = (
        "го!",
    )