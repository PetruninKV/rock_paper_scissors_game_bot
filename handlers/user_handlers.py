from aiogram import Router
from aiogram.filters import CommandStart, Command, Text
from aiogram.types import Message
from keyboards.keyboards import yes_no_kb, game_kb
from lexicon.lexicon_ru import LEXICON_RU


router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)

@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

@router.message(Text(text=LEXICON_RU['yes_button']))
async def yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

@router.message(Text(text=LEXICON_RU['no_button']))
async def no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])

