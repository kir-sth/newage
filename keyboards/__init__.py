from .common import *
from .questioning import *


start = Start(
    greating = "Привет! Это бот для поиска знакомств",
    agreement = "Продолжая, ты подтверждаешь согласие с пользовательским соглашением и правилами конфиденциальности",
    options = (
        "оки",
    )
)

stop = Stop(
    goodbye="Хорошо! Приходи позже"
)

start_question = ClosedQuestion(
    text = "Отлично! Давай начнем заполнять твою анкету?",
    options = (
        "Давай заполним!",
    )
)

goal_question = ClosedQuestion(
    text = "Кого ты хочешь найти?",
    options = (
        "знакомства/друзей",
        "партнера"
    )
)

gender_question = ClosedQuestion(
    text = "Теперь определимся с полом",
    options = (
        "Я девушка",
        "Я парень",
        "Не хочу выбирать"
    )
)

preference_question = ClosedQuestion(
    text = "Кто тебе интересен?",
    options = (
        "Девушки",
        "Парни",
        "Все"
    )
)

name_question = Question(text="Как тебя зовут?")
age_question = Question(text= "Сколько тебе лет?")
description_question = Question(text="Напиши описание своей анкеты")
photo_question = Question(text="Приложи 1 фото к своей анкете")

uploading_photo = UploadingPhoto(
    text = "Поймал твое фото!",
    first = "Ты приложил 1/3 фото. Можешь загрузить еще фото или закончить оформление анкеты",
    second = "Ты приложил 2/3 фото. Можешь загрузить еще фото или закончить оформление анкеты",
    third = "Ты приложил 3/3 фото. Пора закончить оформление анкеты",
    options = (
        "закончить",
    )
)

final_form = FinalForm(
    text = "Вот твоя итоговая анкета",
    options = {
        "отлично!",
    }
)

end_question = ClosedQuestion(
    text = "Начнем поиск знакомств!",
    options = (
        "го!",
    )
)