import random


class Dice:
    """Represents a 6-sided dice."""

    def roll(self):
        """Roll the dice and return the result (1-6)."""
        return random.randint(1, 6)
