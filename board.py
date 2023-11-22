from cards import card
from typing import List

class board:
    def __init__(self, cards_table: List[card], cards_offset: List[card]):
        self.cards_table = cards_table
        self.cards_offset = cards_offset
    
