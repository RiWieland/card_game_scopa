
class card:
    '''
    Class for card
    '''
    def __init__(self, symbol: str, value: int):
        self.symbol = symbol
        self.value = value
    
    def __str__(self):
        return f'Card("{self.symbol}", "{self.value}")'


class card_offset(card):
    '''
    cards that are thrown away
    '''
    def __init__(self):
        super().__init__

class card_open(card):
    '''
    card on the hand of the player
    '''    
    def __init__(self):
        self._registry.append(self)
        super().__init__


class card_player(card):
    '''
    card on the hand of the player
    '''    
    def __init__(self):
        super().__init__

        

