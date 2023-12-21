import random
import itertools
from typing import List
from cards import card

def create_deck() -> list:
    '''
    create deck
    '''
    symbol = ['Swords',	'Cups',	'Coins', 'Batons']
    values = [*range(1, 11, 1)]
    deck = []
    for element in itertools.product(symbol, values):
        deck.append(card(element[0], element[1]))
    return deck

def print_deck(deck: List[card]):
    for card_ in deck:
        print(card_)

def draw_random_card(deck: List[card]) -> card:
    card_ = random.choice(deck)   
    return card_

def remove_cards_idx(deck: List[card], *remove_idx) -> List[card]:
    update_deck = []
    if remove_idx != 0:
        update_deck = deck.pop(remove_idx)
    if remove_card != card("",0):
        update_deck = deck.remove(remove_card)

    return update_deck

def remove_card_from_deck(deck: List[card], remove_card: card) -> List[card]:
    deck.remove(remove_card)
    return deck

def add_card_to_deck(deck: List[card], card):
    return deck.append(card)

def shuffle(deck:List[card]):
        '''
        shuffles the deck
        '''
        random.shuffle(deck)
        return deck

def serve_player_cards(deck:List[card]) -> (List[card],List[card],List[card]):
    '''
    - when called the dealer passes cards to player
    - cards are removed from the deck
    '''
    player_1_cards = []
    player_2_cards = []
    idx_list = []
    for idx, card_ in enumerate(itertools.islice(deck, 6)):
        if (idx % 2) == 0:
            player_1_cards.append(card_)
            idx_list.append(idx)
        else:
            player_2_cards.append(card_)
            idx_list.append(idx)

    remaining_deck = deck[max(idx_list)+1:]
    return remaining_deck, player_1_cards, player_2_cards

def serve_board_deck(deck: List[card], num:int=4)->(List[card],List[card]):
    '''
    fills cards on the board
    '''
    board_cards = []
    idx_list = []
    for idx, card_ in enumerate(itertools.islice(deck, 4)):
        board_cards.append(card_)
        idx_list.append(idx)
    remaining_deck = deck[max(idx_list)+1:]
    return remaining_deck, board_cards

def get_values(cards= List[card]) -> list:

    return [x.value for x in cards ]