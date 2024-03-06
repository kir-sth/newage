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
    goal = State()
    gender = State()
    preference = State()
    name = State()
    age = State()
    description = State()
    uploading_photo = State()
    first_photo = State()
    second_photo = State()
    third_photo = State()
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
    await state.set_state(Questionnaire.goal)


# gender question
@router.message(
    Questionnaire.goal, 
    F.text.in_(messages.goal_question.options)
)
async def gender_handler(message: Message, state: FSMContext):
    await state.update_data(goal=message.text.lower())
    await message.answer(
        text=messages.gender_question.text,
        reply_markup=keyboards.gender_question()
    )
    await state.set_state(Questionnaire.gender)


# preference question
@router.message(
    Questionnaire.gender,
    F.text.in_(messages.gender_question.options)
)
async def preference_handler(message: Message, state: FSMContext):
    await state.update_data(gender=message.text.lower())
    await message.answer(
        text=messages.preference_question.text,
        reply_markup=keyboards.preference_question()
    )
    await state.set_state(Questionnaire.preference)



# name question
@router.message(
    Questionnaire.preference,
    F.text.in_(messages.preference_question.options)
)
async def name_handler(message: Message, state: FSMContext):
    await state.update_data(preference=message.text.lower())
    await message.answer(
        text=messages.name_question.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Questionnaire.name)


# age question
@router.message(
    Questionnaire.name
)
async def age_handler(message: Message, state: FSMContext):
    await state.update_data(name=message.text.lower())
    await message.answer(
        text=messages.age_question.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Questionnaire.age)


# description question
@router.message(
    Questionnaire.age,
    F.text.isdigit
)
async def description_handler(message: Message, state: FSMContext):
    age = int(message.text)
    await state.update_data(age=age)
    await message.answer(
        text=messages.description_question.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Questionnaire.description)


# photo question
@router.message(
    Questionnaire.description
)
async def photo_handler(message: Message, state: FSMContext):
    await state.update_data(description=message.text.lower())
    await message.answer(
        text=messages.photo_question.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Questionnaire.uploading_photo)


# first photo
@router.message(
    Questionnaire.uploading_photo,
    F.photo
)
async def first_photo_handler(message: Message, state: FSMContext):
    await state.update_data(first_photo=message.photo[-1].file_id)
    await message.answer(
        text=messages.uploading_photo.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=messages.uploading_photo.first,
        reply_markup=keyboards.uploading_photo()
    )
    await state.set_state(Questionnaire.first_photo)


# second photo
@router.message(
    Questionnaire.first_photo,
    F.photo
)
async def second_photo_handler(message: Message, state: FSMContext):
    await state.update_data(second_photo=message.photo[-1].file_id)
    await message.answer(
        text=messages.uploading_photo.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=messages.uploading_photo.second,
        reply_markup=keyboards.uploading_photo()
    )
    await state.set_state(Questionnaire.second_photo)


# third photo
@router.message(
    Questionnaire.second_photo,
    F.photo
)
async def second_photo_handler(message: Message, state: FSMContext):
    await state.update_data(third_photo=message.photo[-1].file_id)
    await message.answer(
        text=messages.uploading_photo.text,
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text=messages.uploading_photo.third,
        reply_markup=keyboards.uploading_photo()
    )
    await state.set_state(Questionnaire.third_photo)


# final form
@router.message(
    F.text.in_(messages.uploading_photo.options)
)
async def form_handler(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer_media_group(
        media=messages.form_builder(user_data=user_data),
        reply_markup=keyboards.uploading_photo()
    )
    await state.set_state(Questionnaire.final_form)
