class RightScoreCard:
    def __init__(self):
        self.scores = {
            "three_of_a_kind": None,
            "four_of_a_kind": None,
            "full_house": None,
            "small_straight": None,
            "large_straight": None,
            "yahtzee": None,
            "chance": None,
        }

    def set_score(self, category, dice):
        if category not in self.scores:
            raise ValueError("Invalid category")
        if self.scores[category] is not None:
            raise ValueError(f"{category} already filled")

        if category == "three_of_a_kind":
            self.scores[category] = sum(dice) if self._has_n_of_a_kind(dice, 3) else 0
        elif category == "four_of_a_kind":
            self.scores[category] = sum(dice) if self._has_n_of_a_kind(dice, 4) else 0
        elif category == "full_house":
            self.scores[category] = 25 if self._is_full_house(dice) else 0
        elif category == "small_straight":
            self.scores[category] = 30 if self._is_small_straight(dice) else 0
        elif category == "large_straight":
            self.scores[category] = 40 if self._is_large_straight(dice) else 0
        elif category == "yahtzee":
            self.scores[category] = 50 if len(set(dice)) == 1 else 0
        elif category == "chance":
            self.scores[category] = sum(dice)

    def _has_n_of_a_kind(self, dice, n):
        return any(dice.count(x) >= n for x in dice)

    def _is_full_house(self, dice):
        counts = [dice.count(x) for x in set(dice)]
        return sorted(counts) == [2, 3]

    def _is_small_straight(self, dice):
        unique = sorted(set(dice))
        straights = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]
        return any(s.issubset(unique) for s in straights)

    def _is_large_straight(self, dice):
        unique = sorted(set(dice))
        return unique == [1,2,3,4,5] or unique == [2,3,4,5,6]

    def total(self):
        return sum(v for v in self.scores.values() if v is not None)
