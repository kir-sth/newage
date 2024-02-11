<<<<<<< HEAD
from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.handlers import MessageHandler
from utils import Admin


router = Router()
admin = Admin()
=======
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()
>>>>>>> 16333f6 (reverse)


@router.message(Command("start"))
async def start_handler(msg: Message):
<<<<<<< HEAD
    await msg.answer("Привет!")
    admin.set(msg.chat.id)


@router.message(Command("news"))
async def news_handler(msg: types.Message):
    await msg.answer(f"здесб должны быть новости")



=======
    await msg.answer("Привет! Я помогу тебе узнать твой ID, просто отправь мне любое сообщение")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"Твой ID: {msg.from_user.id}")
>>>>>>> 16333f6 (reverse)
