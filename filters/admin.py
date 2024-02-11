from typing import Tuple

from aiogram.filters import BaseFilter
from aiogram.types import Message


class Verification(BaseFilter):
    def __init__(self, admin_ids: Tuple[int]):
        self.admin_ids = admin_ids

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids
