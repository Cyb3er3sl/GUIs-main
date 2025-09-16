from scorecard import Scorecard

def test_full_house():
    test_sc = Scorecard()
    round_score = test_sc.score_full_house([1, 2, 3, 4, 5])
    assert round_score == 0     
    assert test_sc.score == 0


    test_sc = Scorecard()
    round_score = test_sc.score_full_house([1, 2, 2, 1, 1])
    assert round_score == 25  
    assert test_sc.score == 25


    test_sc = Scorecard()
    round_score = test_sc.score_full_house([2, 2, 2, 1, 1])
    assert round_score == 25
    assert test_sc.score == 25


    test_sc = Scorecard()
    round_score = test_sc.score_full_house([1, 1, 1, 1, 1])
    assert round_score == 0
    assert test_sc.score == 0


def test_score_after_full_house():
    test_sc = Scorecard()
    test_sc.full_house = 0   

    round_score = test_sc.score_full_house([1, 1, 2, 2, 2])
    assert round_score == "Full house already used"
