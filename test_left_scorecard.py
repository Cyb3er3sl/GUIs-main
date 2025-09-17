import pytest
from left_scorecard import LeftScoreCard

def test_basic_scoring():
    s = LeftScoreCard()
    s.set_score("fives", [5,5,2,3,1])
    assert s.scores["fives"] == 10

def test_bonus():
    s = LeftScoreCard()
    s.scores = {"ones": 3, "twos": 6, "threes": 9,
                "fours": 12, "fives": 15, "sixes": 18}
    assert s.total() == 63
    assert s.bonus() == 35
    assert s.grand_total() == 98
