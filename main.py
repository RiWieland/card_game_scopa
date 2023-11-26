

from cards import card, card_offset
from dealer import dealer
from pprint import pprint
from typing import List
from utils import print_deck, draw_random_card
from players import player
from board import board
# round one

if __name__ == "__main__":
    '''
    Every round takes place in main
    '''
    
    dealer_ = dealer() 

    # deck = dealer_.create_deck()
    final_deck, palyer_cards_1, player_cards_2, cards_open = dealer_.start_game()

    player_a = player(palyer_cards_1, [])
    player_b = player(palyer_cards_1, [])
    board_ = board(cards_open)
    print(board_)   







