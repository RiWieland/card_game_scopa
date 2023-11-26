from cards import card, card_open, card_offset
from typing import List

class board:
    def __init__(self, cards_open: List[card_open]):
        self.cards_open = cards_open

    def __str__(self):
        '''
        function prints the board with the information that is observable for the player
        '''

        return f'Cards("{self.cards_open[0]}", "{self.cards_open[1]}", "{self.cards_open[2]}", "{self.cards_open[3]}")'

    
