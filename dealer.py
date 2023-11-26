import itertools
import random
from typing import List
from cards import card, card_player, card_offset, card_open
from utils import remove_card, remove_cards_idx,shuffle,serve_board_deck,serve_player_cards

class dealer:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self) -> list:
        '''
        create deck
        '''
        symbol = ['Swords',	'Cups',	'Coins', 'Batons']
        values = [*range(1, 11, 1)]

        deck = []
        for element in itertools.product(symbol, values):
            deck.append(card(element[0], element[1]))

        return deck
    
    def shuffles(self) -> List[card]:
        '''
        shuffles the deck
        '''
        shuffle_deck = random.shuffle(self.deck)
        return shuffle_deck

    def start_game(self) -> (List[card_player], List[card_player], List[card_open]) :
        '''
        Start game contains 
        - shuffling
        - assign cards to players
        - assign cards to board
        '''
        self.deck = shuffle(self.deck)

        self.deck, cards_open = serve_board_deck(self.deck)
        final_deck, palyer_cards_1, player_cards_2 = serve_player_cards(self.deck)

        return final_deck, palyer_cards_1, player_cards_2, cards_open
    
class deck:
    def __init__(self, deck: List[card]):
        self.deck = deck

    def __str__(self):
        return f'Card("{self.symbol}", "{self.value}")'
    
