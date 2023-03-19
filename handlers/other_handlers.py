from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU

router: Router = Router()

@router.message()
async def other_message(message: Message):
    await message.answer(LEXICON_RU['other_answer'])

    