import itertools
from typing import List
from cards import card
# defintion of neapolitanian cards:

class dealer:
    def create_deck() -> list:
        symbol = ['Swords',	'Cups',	'Coins', 'Batons']
        values = [*range(1, 11, 1)]

        deck = []
        for element in itertools.product(symbol, values):
            deck.append(card(element[0], element[1]))
        return deck

    def start_game():
        return
    
class deck:
    def __init__(self, deck: List[card]):
        self.deck = deck

    def __str__(self):
        return f'Card("{self.symbol}", "{self.value}")'
