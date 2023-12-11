import pytest
from src.card import Card
class TestCard:

    def test_suit_must_be_valid(self):
        with pytest.raises(ValueError):
            c = Card("Not a Suit", 1)

    def test_higher_value_beats_lower_value(self):
        high_card = Card("Hearts", 4)
        low_card = Card("Hearts", 2)
        assert high_card.beats(low_card)