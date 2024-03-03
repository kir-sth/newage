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
    text = "Напиши описание своей анкеты тесктом"


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
