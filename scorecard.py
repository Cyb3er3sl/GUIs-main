from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from die import Die


class Scorecard:
    def __init__(self):
        self.score = 0
        self.used_categories = set()
        self.ones = None
        self.full_house = None

    def _get_values(self, dice):
        """Helper: normalize to list of ints"""
        return [die.value if hasattr(die, "value") else die for die in dice]

    def score_ones(self, dice) -> int | str:
        if "ones" in self.used_categories:
            return "Ones already used"

        dice_vals = self._get_values(dice)
        round_score = sum(val for val in dice_vals if val == 1)

        self.score += round_score
        self.ones = round_score
        self.used_categories.add("ones")
        return round_score

    def score_full_house(self, dice) -> int | str:
        if "full_house" in self.used_categories:
            return "Full house already used"

        values = self._get_values(dice)
        values.sort()

        if (values[0] == values[1] and values[2] == values[3] and values[3] == values[4]):
            round_score = 25
        elif (values[0] == values[1] and values[1] == values[2] and values[3] == values[4]):
            round_score = 25
        else:
            round_score = 0

        self.score += round_score
        self.full_house = round_score
        self.used_categories.add("full_house")
        return round_score
