from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command
from filters.admin import Verification


ADMINS=(
    538855523,
)

router = Router()
router.message.filter(
    Verification(admin_ids=ADMINS)
)


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет!")


@router.message(Command("news"))
async def news_handler(msg: types.Message):
    await msg.answer(f"здесб должны быть новости")
