from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU

button1: KeyboardButton = KeyboardButton(text=LEXICON_RU["yes_button"])
button2: KeyboardButton = KeyboardButton(text=LEXICON_RU["no_button"])

yes_no_kb_buider: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

yes_no_kb_buider.row(button1, button2, width=2)

yes_no_kb = yes_no_kb_buider.as_markup( 
                                    one_time_keyboard=True,
                                    resize_keyboard=True)



button1: KeyboardButton = KeyboardButton(text=LEXICON_RU["rock"])
button2:KeyboardButton = KeyboardButton(text=LEXICON_RU["scissors"])
button3:KeyboardButton = KeyboardButton(text=LEXICON_RU["paper"])

game_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup( 
                                                keyboard=[[button1], [button2],[button3]],
                                                resize_keyboard=True)


