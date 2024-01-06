from pydantic import BaseModel
from typing import List

from cards import card

class export_card_class(BaseModel):
    cards: List[card]
