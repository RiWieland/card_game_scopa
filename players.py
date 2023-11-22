from typing import List
from cards import card, card_player, card_offset

class player:
    def __init__(self, cards_hand:List[card_player], cards_offset:List[card_offset]):
        self.cards_hand = cards_hand

