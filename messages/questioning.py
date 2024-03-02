class start_questionnaire():
    message = "Отлично! Давай начнем заполнять твою анкету?"
    answer = "Давай заполним!"


class goal_questionnaire():
    message = "Кого ты хочешь найти?"
    options = (
        "знакомства/друзей",
        "партнера"
    )


class gender_questionnaire():
    message = "Теперь определимся с полом"
    options = (
        "Я девушка",
        "Я парень",
        "Не хочу выбирать"
    )


class preference_questionnaire():
    message = "Кто тебе интересен?"
    options = (
        "Девушки",
        "Парни",
        "Все"
    )