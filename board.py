from cards import card, card_open, card_offset
from typing import List

class board:
    def __init__(self, cards_open: List[card_open], cards_offset: List[card_offset]):
        self.cards_open = cards_open
        self.cards_offset = cards_offset
    
