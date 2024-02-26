from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery


router = Router()


@router.callback_query(F.data == "agreement")
async def start_questionnaire(callback: CallbackQuery):
    await callback.message.answer(
        "Старт заполнения анкеты"
    )

