
import random

class Die:
    def __init__(self):
        self.value = 1
        self.held = False

    def roll(self):
        if not self.held:
            self.value = random.randint(1, 6)
        return self.value

    def toggle_hold(self):
        self.held = not self.held

    def set_hold(self, val: bool):
        self.held = bool(val)

    def __repr__(self):
        return f"<Die value={self.value} held={self.held}>"
