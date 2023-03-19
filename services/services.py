import random
from lexicon.lexicon_ru import LEXICON_RU

game_dict: dict = {
            'rock': LEXICON_RU['rock'],
            'scissors': LEXICON_RU['scissors'],
            'paper': LEXICON_RU['paper']
            }


def get_bot_choice() -> str:
    keys = list(game_dict.keys())
    return random.choices(keys)[0]


def _normalize_user_answer(user_answer: str) -> str:
    for key in game_dict:
        if game_dict[key] == user_answer:
            return key
        

def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rule: dict[str | str] = {   'rock': 'scissors',
                                'scissors': 'paper',
                                'paper': 'rock'}
    
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rule[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
    

