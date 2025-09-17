class LeftScoreCard:
    def __init__(self):
        self.scores = {
            "ones": None,
            "twos": None,
            "threes": None,
            "fours": None,
            "fives": None,
            "sixes": None,
        }

    def set_score(self, category, dice):
        if category not in self.scores:
            raise ValueError("Invalid category")
        if self.scores[category] is not None:
            raise ValueError(f"{category} already filled")

        num = {
            "ones": 1,
            "twos": 2,
            "threes": 3,
            "fours": 4,
            "fives": 5,
            "sixes": 6,
        }[category]

        self.scores[category] = dice.count(num) * num

    def total(self):
        return sum(v for v in self.scores.values() if v is not None)

    def bonus(self):
        """35 points bonus if total of upper section >= 63"""
        return 35 if self.total() >= 63 else 0

    def grand_total(self):
        return self.total() + self.bonus()
