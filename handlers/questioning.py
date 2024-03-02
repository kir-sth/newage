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
    choosing_preference = State()


@router.message(F.text == messages.start_handler.options[0])
async def gstart_question(message: Message):
    await message.answer(
        text=messages.start_question.text,
        reply_markup=keyboards.start_question()
    )


@router.message(StateFilter(None), F.text.in_(messages.start_question.options))
async def goal_question(message: Message, state: FSMContext):
    await message.answer(
        text=messages.goal_question.text,
        reply_markup=keyboards.goal_question()
    )
    await state.set_state(Questionnaire.choosing_goal)


@router.message(
    Questionnaire.choosing_goal, 
    F.text.in_(messages.goal_question.options)
)
async def gender_question(message: Message, state: FSMContext):
    await state.update_data(choosing_goal=message.text.lower())
    await message.answer(
        text=messages.gender_question.text,
        reply_markup=keyboards.gender_question()
    )
    await state.set_state(Questionnaire.choosing_gender)


@router.message(
    Questionnaire.choosing_gender,
    F.text.in_(messages.gender_question.options)
)
async def preference_question(message: Message, state: FSMContext):
    await state.update_data(choosing_gender=message.text.lower())
    await message.answer(
        text=messages.preference_question.text,
        reply_markup=keyboards.preference_question()
    )
    await state.set_state(Questionnaire.choosing_preference)
