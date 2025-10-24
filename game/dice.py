import random


class Dice:
    """6-sided dice supporting optional cheat roll."""

    def roll(self, cheat_number=None):
        """Return a random roll or cheat value."""
        if cheat_number is not None:
            return cheat_number
        return random.randint(1, 6)

