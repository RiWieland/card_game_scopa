import itertools
import random
from typing import List
from cards import card, card_player, card_offset, card_open
from utils import remove_card, remove_cards_idx,shuffle

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
        print(shuffle_deck)
        exit()
        cards_open = shuffle_deck[0:4]
        cards_player_1 = []
        cards_player_2 = []
        print(len(shuffle_deck))
        r = range(1,3)

        shuffle_deck = remove_cards_idx(shuffle_deck,'1','2','3' )
        print(len(shuffle_deck))

        '''

        chunk_size = 3

        for card_ in deck[5:]:
            if len(deck)/2== 0:
                cards_player_1.append(card_)
            else :
                cards_player_2.append(card_)
        '''
        return cards_player_1, cards_player_2, cards_open
    
class deck:
    def __init__(self, deck: List[card]):
        self.deck = deck

    def __str__(self):
        return f'Card("{self.symbol}", "{self.value}")'
    
