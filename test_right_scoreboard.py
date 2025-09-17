import pytest
from right_scorecard import RightScoreCard

def test_three_of_a_kind():
    s = RightScoreCard()
    s.set_score("three_of_a_kind", [2,2,2,4,5])
    assert s.scores["three_of_a_kind"] == 15

def test_full_house():
    s = RightScoreCard()
    s.set_score("full_house", [3,3,2,2,2])
    assert s.scores["full_house"] == 25

def test_small_straight():
    s = RightScoreCard()
    s.set_score("small_straight", [1,2,3,4,6])
    assert s.scores["small_straight"] == 30

def test_large_straight():
    s = RightScoreCard()
    s.set_score("large_straight", [2,3,4,5,6])
    assert s.scores["large_straight"] == 40

def test_yahtzee():
    s = RightScoreCard()
    s.set_score("yahtzee", [6,6,6,6,6])
    assert s.scores["yahtzee"] == 50

def test_chance():
    s = RightScoreCard()
    s.set_score("chance", [1,2,3,4,5])
    assert s.scores["chance"] == 15
