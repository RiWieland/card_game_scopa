from typing import List
from cards import card, card_player, card_offset
from utils import remove_card_from_deck, add_card_to_deck

class player:
    def __init__(self, cards_hand:List[card_player]):
        self.cards_hand = cards_hand

    def put_card_to_card_open(self, card:card):
        '''
        action of putting a specific card to the table
        '''
        if card in self.cards_hand:
            self.cards_hand = remove_card_from_deck(self.cards_hand, card)
        else:
            raise Exception("This card is not a member of the players deck")
            


class player_smart(player):

    def receive_cards_open(self, cards_open:List[card]):
        '''
        observed cards open
        '''
        self.observe_open = cards_open

    def receive_cards_offset(self, cards_offset:List[card]):
        '''
        observed cards in the offset
        '''
        self.observe_offset = cards_offset

    
class player_random(player):
    pass