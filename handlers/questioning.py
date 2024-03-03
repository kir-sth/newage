import keyboards
import messages

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.utils.media_group import MediaGroupBuilder


router = Router()


class Questionnaire(StatesGroup):
    choosing_goal = State()
    choosing_gender = State()
    choosing_preference = State()
    choosing_age = State()
    choosing_description = State()
    choosing_photo = State()
    final_form = State()


# start question
@router.message(F.text == messages.start_handler.options[0])
async def start_handler(message: Message):
    await message.answer(
        text=messages.start_question.text,
        reply_markup=keyboards.start_question()
    )


# goal question
@router.message(StateFilter(None), F.text.in_(messages.start_question.options))
async def goal_handler(message: Message, state: FSMContext):
    await message.answer(
        text=messages.goal_question.text,
        reply_markup=keyboards.goal_question()
    )
    await state.set_state(Questionnaire.choosing_goal)


# gender question
@router.message(
    Questionnaire.choosing_goal, 
    F.text.in_(messages.goal_question.options)
)
async def gender_handler(message: Message, state: FSMContext):
    await state.update_data(choosing_goal=message.text.lower())
    await message.answer(
        text=messages.gender_question.text,
        reply_markup=keyboards.gender_question()
    )
    await state.set_state(Questionnaire.choosing_gender)


# preference question
@router.message(
    Questionnaire.choosing_gender,
    F.text.in_(messages.gender_question.options)
)
async def preference_handler(message: Message, state: FSMContext):
    await state.update_data(choosing_gender=message.text.lower())
    await message.answer(
        text=messages.preference_question.text,
        reply_markup=keyboards.preference_question()
    )
    await state.set_state(Questionnaire.choosing_preference)


# age question
@router.message(
    Questionnaire.choosing_preference,
    F.text.in_(messages.preference_question.options)
)
async def age_handler(message: Message, state: FSMContext):
    await state.update_data(choosing_preference=message.text.lower())
    await message.answer(
        text=messages.age_question.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Questionnaire.choosing_age)


# description question
@router.message(
    Questionnaire.choosing_age,
    F.text.isdigit
)
async def description_handler(message: Message, state: FSMContext):
    age = int(message.text)
    await state.update_data(choosing_age=age)
    await message.answer(
        text=messages.description_question.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Questionnaire.choosing_description)


# photo question
@router.message(
    Questionnaire.choosing_description
)
async def photo_handler(message: Message, state: FSMContext):
    await state.update_data(choosing_description=message.text.lower())
    await message.answer(
        text=messages.photo_question.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Questionnaire.choosing_photo)


# first photo
@router.message(
    Questionnaire.choosing_photo,
    F.photo
)
async def first_photo_handler(message: Message, state: FSMContext):
    await state.update_data(choosing_photo=F.photo[-1])
    await message.answer(
        text=messages.first_photo.text[0],
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=messages.first_photo.text[1],
        reply_markup=keyboards.first_photo_getter()
    )
    await state.set_state(Questionnaire.choosing_photo)


# final form
@router.message(
    Questionnaire.choosing_photo,
    F.text == "закончить"
)
async def form_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()
    text=messages.form_builder(user_data=user_data)
    await message.answer(
        text=text
    )
    await state.set_state(Questionnaire.final_form)
