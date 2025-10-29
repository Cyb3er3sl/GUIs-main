import pytest
from scorecard import Scorecard


def test_score_ones_basic():
    sc = Scorecard()
    assert sc.score_ones([1, 1, 2, 3, 4]) == 2
    assert sc.score == 2

def test_score_ones_all_ones():
    sc = Scorecard()
    result = sc.score_ones([1, 1, 2, 1, 1])
    assert result == 4
    assert sc.score == 4

def test_score_ones_no_ones():
    sc = Scorecard()
    result = sc.score_ones([5, 5, 5, 5, 5])
    assert result == 0
    assert sc.score == 0

def test_score_ones_already_used():
    sc = Scorecard()
    sc.score_ones([1, 1, 1, 1, 1])
    result = sc.score_ones([1, 1, 2, 3, 4])
    assert result == "Ones already used"


def test_full_house_valid():
    sc = Scorecard()
    result = sc.score_full_house([3, 3, 2, 2, 2])
    assert result == 25
    assert sc.score == 25

def test_full_house_reverse_valid():
    sc = Scorecard()
    result = sc.score_full_house([2, 2, 2, 3, 3])
    assert result == 25
    assert sc.full_house == 25

def test_full_house_invalid():
    sc = Scorecard()
    result = sc.score_full_house([1, 2, 3, 4, 5])
    assert result == 0
    assert sc.score == 0

def test_full_house_already_used():
    sc = Scorecard()
    sc.score_full_house([3, 3, 3, 2, 2])
    result = sc.score_full_house([2, 2, 2, 3, 3])
    assert result == "Full house already used"


def test_score_with_die_objects():
    class MockDie:
        def __init__(self, value): self.value = value
    dice = [MockDie(v) for v in [1, 1, 2, 3, 4]]
    sc = Scorecard()
    result = sc.score_ones(dice)
    assert result == 2
    assert sc.score == 2
