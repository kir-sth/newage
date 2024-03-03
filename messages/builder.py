from aiogram.utils.media_group import MediaGroupBuilder
from typing import Dict, Any


def form_builder(user_data: Dict[str, Any]) -> str:
    goal = user_data["choosing_goal"]
    age = user_data["choosing_age"]
    gender = user_data["choosing_gender"]
    prefernce= user_data["choosing_preference"]
    description = user_data["choosing_description"]
    text=f"{goal}\n{age}\n{gender}\n{prefernce}\n{description}"
    return text