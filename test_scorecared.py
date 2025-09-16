from scorecard import Scorecard
 
 
def test_score_ones():
    testing_sc = Scorecard()
    score = testing_sc.score_ones([1,1,2,3,4])
    assert score == 2
 
    testing_sc = Scorecard()
    score = testing_sc.score_ones([1,1,2,1,1])
    assert score == 4
 
    testing_sc = Scorecard()
    score = testing_sc.score_ones([5,5,5,5,5])
    assert score == 0
 
def test_try_to_score_after_scoring():
    testing_sc = Scorecard()
    score = testing_sc.score_ones([1,1,2,3,4])
    assert score == 2
 
    score = testing_sc.score_ones([1,1,2,1,1])
    assert score == "Ones already used"