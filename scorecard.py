from collections import Counter
from typing import List, Optional, Dict

CATEGORIES = [
    "ones", "twos", "threes", "fours", "fives", "sixes",
    "three_of_a_kind", "four_of_a_kind", "full_house",
    "small_straight", "large_straight", "yahtzee", "chance"
]

class Scorecard:
    def __init__(self):
        self.scores: Dict[str, Optional[int]] = {c: None for c in CATEGORIES}

    def available_categories(self):
        return [c for c, s in self.scores.items() if s is None]

    @staticmethod
    def counts(dice: List[int]) -> Counter:
        return Counter(dice)

    @staticmethod
    def upper_number_score(dice: List[int], face: int) -> int:
        return sum(d for d in dice if d == face)

    @staticmethod
    def three_of_a_kind_score(dice: List[int]) -> int:
        if any(v >= 3 for v in Counter(dice).values()):
            return sum(dice)
        return 0

    @staticmethod
    def four_of_a_kind_score(dice: List[int]) -> int:
        if any(v >= 4 for v in Counter(dice).values()):
            return sum(dice)
        return 0

    @staticmethod
    def full_house_score(dice: List[int]) -> int:
        vals = sorted(Counter(dice).values())
        return 25 if vals == [2, 3] else 0

    @staticmethod
    def small_straight_score(dice: List[int]) -> int:
        s = set(dice)
        straights = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]
        return 30 if any(st.issubset(s) for st in straights) else 0

    @staticmethod
    def large_straight_score(dice: List[int]) -> int:
        s = set(dice)
        return 40 if s in ({1,2,3,4,5}, {2,3,4,5,6}) else 0

    @staticmethod
    def yahtzee_score(dice: List[int]) -> int:
        return 50 if len(set(dice)) == 1 else 0

    @staticmethod
    def chance_score(dice: List[int]) -> int:
        return sum(dice)

    @staticmethod
    def score_for_category(dice: List[int], category: str) -> int:
        if category == "ones": return Scorecard.upper_number_score(dice, 1)
        if category == "twos": return Scorecard.upper_number_score(dice, 2)
        if category == "threes": return Scorecard.upper_number_score(dice, 3)
        if category == "fours": return Scorecard.upper_number_score(dice, 4)
        if category == "fives": return Scorecard.upper_number_score(dice, 5)
        if category == "sixes": return Scorecard.upper_number_score(dice, 6)
        if category == "three_of_a_kind": return Scorecard.three_of_a_kind_score(dice)
        if category == "four_of_a_kind": return Scorecard.four_of_a_kind_score(dice)
        if category == "full_house": return Scorecard.full_house_score(dice)
        if category == "small_straight": return Scorecard.small_straight_score(dice)
        if category == "large_straight": return Scorecard.large_straight_score(dice)
        if category == "yahtzee": return Scorecard.yahtzee_score(dice)
        if category == "chance": return Scorecard.chance_score(dice)
        raise ValueError(f"Unknown category: {category}")

    def set_score(self, category: str, dice: List[int]) -> int:
        if category not in self.scores:
            raise ValueError("Invalid category")
        if self.scores[category] is not None:
            raise ValueError("Category already scored")
        val = self.score_for_category(dice, category)
        self.scores[category] = val
        return val

    def total_upper(self) -> int:
        return sum(self.scores[c] or 0 for c in ["ones","twos","threes","fours","fives","sixes"])

    def upper_bonus(self) -> int:
        return 35 if self.total_upper() >= 63 else 0

    def total_lower(self) -> int:
        lower = ["three_of_a_kind","four_of_a_kind","full_house","small_straight","large_straight","yahtzee","chance"]
        return sum(self.scores[c] or 0 for c in lower)

    def grand_total(self) -> int:
        return self.total_upper() + self.upper_bonus() + self.total_lower()
