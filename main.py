

from cards import card, card_offset
from dealer import dealer
from pprint import pprint
from typing import List
from utils import print_deck, draw_random_card

# round one

if __name__ == "__main__":
    
    deck = dealer.create_deck()
    print(len(deck))

    dealer.start_game(deck)    

    c1 = card("caro", "2")
    c2 = card("pik", "4")

    list_cards = [c1, c2]
    print(type(c1))
    c1.__class__ = card_offset
    print(c1.value)

    print_deck(deck)
    print(draw_random_card(deck))




