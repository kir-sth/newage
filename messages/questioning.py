from typing import Dict, Any


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


class age_question():
    text = "Сколько тебе лет?"


class description_question():
    text = "Напиши описание своей анкеты"


class photo_question():
    text = "Приложи 1 фото к своей анкете"


class first_photo():
    text = (
        "Поймал твое фото",
        "Ты приложил 1/3 фото. Хочешь приложить еще одно или закончить оформление анкеты?"
    )
    options = (
        "закончить",
    )


def form_builder(user_data: Dict[str, Any]) -> str:
    goal = user_data["goal"]
    age = user_data["age"]
    gender = user_data["gender"]
    prefernce= user_data["preference"]
    description = user_data["description"]
    text=f"{goal}\n{age}\n{gender}\n{prefernce}\n{description}"
    return text
