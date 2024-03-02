import keyboards
import messages

from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        messages.start_handler_text.greating
    )
    await msg.answer(
        messages.start_handler_text.agreement,
        reply_markup=keyboards.agreement()
    )


@router.message(Command("stop"))
async def stop_handler(msg: Message):
    await msg.answer(
        messages.stop_handler_text.goodbye,
        reply_markup=ReplyKeyboardRemove()
    )
