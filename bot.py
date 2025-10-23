<<<<<<< HEAD
"""The module containing the computer intelligence of the game."""

=======
>>>>>>> Jeyson
import random
from player import Player


<<<<<<< HEAD
class ComputerPlayer(Player):
    """Represent a computer player with different levels of difficulty."""

    def __init__(self, name, intelligence="normal"):
        """Initialize the computer player with name and intelligence level."""
        super().__init__(name)
        self.intelligence = intelligence.lower()
=======

class ComputerPlayer:
    """Represents a computer-controlled player."""

    def __init__(self, name, intelligence="normal"):
        self.name = name
        self.total_score = 0
        self.current_score = 0
        self.intelligence = intelligence
>>>>>>> Jeyson

    def reset_turn(self):
        """Reset the computer player's current score."""
        self.current_score = 0

    def add_to_total(self):
        """Add the current score to total score."""
        self.total_score += self.current_score
        self.current_score = 0

    def decide(self):
<<<<<<< HEAD
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
=======
        """Decide whether to 'roll' or 'hold' based on intelligence level."""
        if self.intelligence == "easy":
            return "roll" if random.random() < 0.75 else "hold"
        elif self.intelligence == "normal":
            return "roll" if self.current_score < 20 else "hold"
        else:  # hard level
            return "roll" if self.current_score < 30 else "hold"
>>>>>>> Jeyson
