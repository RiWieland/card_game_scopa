from fastapi import FastAPI


from cards import card, card_offset, card_open
from dealer import dealer
from pprint import pprint
from typing import List

from utils import print_deck, random_card, create_deck
from players import player, player_smart, player_random
from game_logic import get_all_players_cards
from board import board
#from export_classes import export_card_class


# init dealer and serve cards
dealer_ = dealer.get_deck(deck=create_deck())
play_deck, player_cards_1, player_cards_2, cards_open = dealer_.initial_serve()
board_ = board(cards_open)

# init players
player_smart_ = player_smart(player_cards_1)
player_random_ = player_random(player_cards_2)

# Round one: Both player play card

player_random_.play_card(random_card(player_random_.cards_hand))
board_.add_card_to_cards_open(random_card(player_smart_.cards_hand))

player_smart_.play_card(random_card(player_smart_.cards_hand))
board_.add_card_to_cards_open(random_card(player_smart_.cards_hand))




print((player_smart_.cards_hand))




app = FastAPI()

@app.get("/api/v1/cards")
async def get_players_card():
    return all_cards(List[export_card_class])
