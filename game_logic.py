'''
file for the game logic 
'''

from typing import List

from cards import card, card_player, card_offset, card_open


def return_card_match(cards_open:List[card], cards_player:List[card] ):
    '''
    check if its possbile to match open_cards and player_cards
    '''
    return list(set(cards_open).intersection(cards_player))