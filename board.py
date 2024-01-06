from cards import card, card_open, card_offset
from typing import List

class board:
    def __init__(self, cards_open_: List[card_open], cards_offset_):
        self.cards_open = cards_open_
        self.cards_offset = cards_offset_

    def __str__(self):
        '''
        function prints the board with the information that is observable for the player
        '''

        return f'Cards("{self.cards_open[0]}", "{self.cards_open[1]}", "{self.cards_open[2]}", "{self.cards_open[3]}")'

    def add_card_to_cards_open(self, card_:card):
        self.cards_open.append(card_)

    def add_card_to_cards_offset(self, card_:card):
        self.cards_offset.append(card_)
