from aiogram import types, Router, F
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет!")


@router.message(F.voice.as_("largest_photo"))
async def start_handler(msg: Message):
    await msg.answer("Поймал твоё аудио")
