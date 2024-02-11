from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.handlers import MessageHandler
from utils import Admin


router = Router()
admin = Admin()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет!")
    admin.set(msg.chat.id)


@router.message(Command("news"))
async def news_handler(msg: types.Message):
    await msg.answer(f"здесб должны быть новости")



