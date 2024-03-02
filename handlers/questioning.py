import keyboards
import messages

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext


router = Router()


class Questionnaire(StatesGroup):
    choosing_goal = State()
    choosing_gender = State()
    choosing_preferences = State()


@router.callback_query(F.data == "agreement")
async def start_questionnaire(callback: CallbackQuery):
    await callback.message.answer(
        messages.start_questionnaire_text.message,
        reply_markup=keyboards.start_questionnaire()
    )


@router.message(StateFilter(None), F.text == messages.start_questionnaire_text.answer)
async def goal_questionnaire(message: Message, state: FSMContext):
    await message.answer(
        messages.goal_questionnaire_text.message,
        reply_markup=keyboards.goal_questionnaire()
    )
    await state.set_state(Questionnaire.choosing_goal)
