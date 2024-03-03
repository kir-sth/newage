from aiogram.utils.media_group import MediaGroupBuilder
from typing import Dict, Any


def form_builder(user_data: Dict[str, Any]) -> str:
    goal = user_data["goal"]
    age = user_data["age"]
    gender = user_data["gender"]
    prefernce= user_data["preference"]
    description = user_data["description"]
    text=f"{goal}\n{age}\n{gender}\n{prefernce}\n{description}"
    return text