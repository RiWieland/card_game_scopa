import random

from typing import List
from cards import card

def print_deck(deck: List[card]):
    for card_ in deck:
        print(card_)

def draw_random_card(deck: List[card]) -> card:
    card_ = random.choice(deck)   
    return card_

def remove_cards_idx(deck: List[card], *remove_idx) -> List[card]:
    update_deck = []
    if remove_index != 0:
        update_deck = deck.pop(remove_index)
    if remove_card != card("",0):
        update_deck = deck.remove(remove_card)

    return update_deck

def remove_card(deck: List[card], remove_card: card = card("",0), *remove_idx) -> List[card]:
    update_deck = []
    if remove_index != 0:
        update_deck = deck.pop(remove_index)
    if remove_card != card("",0):
        update_deck = deck.remove(remove_card)

    return update_deck

def shuffle(deck:List[card]):
        '''
        shuffles the deck
        '''
        random.shuffle(deck)
        return deck
