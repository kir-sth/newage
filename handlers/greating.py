import keyboards
import messages

from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        text=messages.start_handler.greating
    )
    await msg.answer(
        text=messages.start_handler.agreement,
        reply_markup=keyboards.agreement()
    )


@router.message(Command("stop"))
async def stop_handler(msg: Message):
    await msg.answer(
        text=messages.stop_handler.goodbye,
        reply_markup=ReplyKeyboardRemove()
    )
