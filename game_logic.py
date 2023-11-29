'''
file for the game logic 
'''

from typing import List
from utils import get_values

from cards import card, card_player, card_offset, card_open


def return_card_match(cards_open:List[card], cards_player:List[card]) -> list:
    '''
    check if its possbile to match open_cards and player_cards
    '''
    return list(set(cards_open).intersection(cards_player))

def prob_scopa_this_round(card_open:List[card], card_offset:List[card], cards_player_own:List[card], cards_player_other:List[card]) ->float:
    '''
    calcualte probability of a scopa for the other player
    at the moment one round 
    '''
    if len(card_open)==1:
        value = card_open[0].value
        num_offset = get_values(card_offset).count(value)
        num_player = get_values(cards_player_own).count(value)
        remain = 4 - (num_offset + num_player)
        total = 40 - len(card_open)+ len(card_offset) + len(cards_player_own) + len(cards_player_other)
        prob = remain/total *len(cards_player_other)
    else:
        pass
    return prob
