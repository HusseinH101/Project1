"""The module containing the computer intelligence of the game."""

import random
from player import Player


class ComputerPlayer(Player):
    """Represent a computer player with different levels of difficulty."""

    def __init__(self, name, intelligence="normal"):
        """Initialize the computer player with name and intelligence level."""
        super().__init__(name)
        self.intelligence = intelligence.lower()

    def decide(self):
        """Decide the computer's action based on difficulty level.

        Returns:
            str: "roll" to throw the dice or "hold" to save points.
        """
        if self.intelligence == "easy":
            return random.choice(["roll", "hold"])

        if self.intelligence == "normal":
            return "hold" if self.current_score >= 20 else "roll"

        if (
            self.current_score + self.total_score >= 100
            or self.current_score >= 25
        ):
            return "hold"

        return "roll"
