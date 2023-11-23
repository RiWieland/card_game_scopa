import random

from typing import List
from cards import card

def print_deck(deck: List[card]):
    for card_ in deck:
        print(card_)

def draw_random_card(deck: List[card]) -> card:
    card_ = random.choice(deck)   
    return card_