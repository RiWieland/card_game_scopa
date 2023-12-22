

from cards import card, card_offset
from dealer import dealer
from pprint import pprint
from typing import List
from utils import print_deck, random_card, create_deck
from players import player_smart, player_random
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

    play_deck, player_cards_1, player_cards_2, cards_open = dealer_.initial_serve()

    player_smart_ = player_smart(player_cards_1)
    player_random_ = player_random(player_cards_2)
    board_ = board(cards_open)
    
    # Round one:
    player_random_.play_card(random_card(player_random_.cards_hand))
    board_.add_card_to_cards_open(random_card(player_smart_.cards_hand))

    # player_smart plays also random
    player_smart_.play_card(random_card(player_smart_.cards_hand))
    board_.add_card_to_cards_open(random_card(player_smart_.cards_hand))


