

from cards import card, card_offset
from dealer import dealer
from pprint import pprint
from typing import List
from utils import print_deck, draw_random_card, create_deck
from players import player
from board import board
# round one

# todo:
# # fabric 
#  - for serve
# - for player init: one random, one intelligent one
# # @classmethod for init

if __name__ == "__main__":
    '''
    Every round takes place in main
    '''
    
    dealer_ = dealer.get_deck(deck=create_deck())

    final_deck, player_cards_1, player_cards_2, cards_open = dealer_.initial_serve()

    player_a = player(player_cards_1, [])
    player_b = player(player_cards_2, [])
    board_ = board(cards_open)

    print(board_)   







