import itertools
import random
from typing import List
from cards import card, card_player, card_offset, card_open
from utils import remove_card, remove_cards_idx,shuffle,serve_board_deck,serve_player_cards

class dealer:
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
    
    def shuffles(deck:List[card]) -> List[card]:
        '''
        shuffles the deck
        '''
        shuffle_deck = random.shuffle(deck)
        return shuffle_deck

    def start_game(deck:List[card]) -> (List[card_player], List[card_player], List[card_open]) :
        '''
        Start game contains 
        - shuffling
        - assign cards to players
        - assign cards to board
        '''
        shuffle_deck = shuffle(deck)

        remaining_deck, cards_open = serve_board_deck(shuffle_deck)
        final_deck, palyer_cards_1, player_cards_2 = serve_player_cards(remaining_deck)

        return final_deck, palyer_cards_1, player_cards_2, cards_open
    
class deck:
    def __init__(self, deck: List[card]):
        self.deck = deck

    def __str__(self):
        return f'Card("{self.symbol}", "{self.value}")'
    
