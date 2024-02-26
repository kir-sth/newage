import keyboards

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(
        "Привет! Это бот для поиска знакомств",
        reply_markup=keyboards.lets_start()
    )


@router.message(F.text == "давай начнем")
async def agreement_handler(msg: Message):
    await msg.answer(
        "Ознакомься с пользовательским соглашением и правилами конфиденциальности",
        reply_markup=keyboards.agreement()
    )


@router.message(Command("stop"))
async def stop_handler(msg: Message):
    await msg.answer(
        "Хорошо! Приходи снова",
        reply_markup=ReplyKeyboardRemove()
    )
