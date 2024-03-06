from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command

from keyboards import (
    start,
    stop
)


router = Router()


@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        text=start.greating
    )
    await message.answer(
        text=start.agreement,
        reply_markup=start.get_keyboard()
    )


@router.message(Command("stop"))
async def stop_handler(message: Message):
    await message.answer(
        text=stop.goodbye,
        reply_markup=ReplyKeyboardRemove()
    )
