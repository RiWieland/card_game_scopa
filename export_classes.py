from pydantic import BaseModel
from typing import List

from cards import card, card_offset

class player_card_class(BaseModel):
    player: str
    cards: List[card]

