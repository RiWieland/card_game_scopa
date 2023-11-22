from typing import List
from cards import card

class player:
    def __init__(self, cards_hand:List[card]):
        self.cards_hand = cards_hand