from typing import List
from cards import card, card_player, card_offset

class player:
    def __init__(self, cards_hand:List[card_player]):
        self.cards_hand = cards_hand

class player_smart(player):
    def receive_cards_open(self, cards_open:List[card]):
        '''
        observed cards open
        '''
        self.observe_open = cards_open
        pass 

    def receive_cards_offset(self, cards_offset:List[card]):
        '''
        observed cards in the offset
        '''
        self.observe_offset = cards_offset
        pass
    

class player_random(player):
    pass