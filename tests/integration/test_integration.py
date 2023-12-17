
import sys
sys.path.append(".") # Adds higher directory to python modules path.

from dealer import dealer
from utils import create_deck

def test_len_initial_serve():
    dealer_ = dealer.get_deck(deck=create_deck())
    play_deck, player_cards_1, player_cards_2, cards_open = dealer_.initial_serve()

    assert len(cards_open) == 4
    assert len(player_cards_1) == 3

