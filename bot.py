import random


class ComputerPlayer:
    """Represents a computer-controlled player."""

    def __init__(self, name, intelligence="normal"):
        self.name = name
        self.total_score = 0
        self.current_score = 0
        self.intelligence = intelligence

    def reset_turn(self):
        """Reset the computer player's current score."""
        self.current_score = 0

    def add_to_total(self):
        """Add the current score to total score."""
        self.total_score += self.current_score
        self.current_score = 0

    def decide(self):
        """Decide whether to 'roll' or 'hold' based on intelligence level."""
        if self.intelligence == "easy":
            return "roll" if random.random() < 0.75 else "hold"
        elif self.intelligence == "normal":
            return "roll" if self.current_score < 20 else "hold"
        else:  # hard level
            return "roll" if self.current_score < 30 else "hold"
