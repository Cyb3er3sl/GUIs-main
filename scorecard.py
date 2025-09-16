from __future__ import annotations
from typing import TYPE_CHECKING, Sequence

if TYPE_CHECKING:
    from die import Die


class Scorecard:
    def __init__(self):
        self.score = 0
        self.ones = None

    def score_ones(self, dice: list[Die]) -> int:
        round_score = 0
        dice_vals = [die.value for die in dice]
        for val in dice_vals:
            if val == 1:
                round_score += 1
        #print(round_score)
        self.score += round_score
        self.ones = round_score
        return round_score
    

    def score_full_house(self, dice: list[Die]):
        round_score = 0
        values =  [die.value for die in dice]
        values.sort()
        
        print(values)
        # For 3, 3, 5, 5, 5
        #         3   ==   3                5      ==     5             5       ==   5
        if (values[0] == values[1]) and (values[2] == values[3]) and (values[3] == values[4]):
            round_score = 25
            
        elif (values[0] == values[1]) and (values[1] == values[2]) and (values[3] == values[4]):
            round_score = 25
        else: 
            round_score = 0

        print(round_score)