from collections import Counter

class Scorecard:
    def __init__(self):
        self.score = 0
        self.full_house_used = False 

    def score_full_house(self, dice):

        if self.full_house_used:
            return "Full house already used"

        counts = sorted(Counter(dice).values())


        if counts == [2, 3]:
            self.full_house_used = True
            self.score += 25
            return 25

        # Not a full house
        self.full_house_used = True
        return 0
