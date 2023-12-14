
class Hand:

    def __init__(self):
        self.cards = []

    @property
    def has_card(self) -> bool:
        return len(self.cards) > 0

    def play_card(self):
        if not self.has_card:
            raise ValueError('cannot play card from empty hand')
        return self.cards.pop()
    
hand = Hand()
hand.has_card