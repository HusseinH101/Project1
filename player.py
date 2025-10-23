class Player:
    """Represents a player in the game."""

    def __init__(self, name):
        self.name = name
        self.current_score = 0
        self.total_score = 0

    def reset_turn(self):
        """Reset the player's current score for the next turn."""
        self.current_score = 0

    def add_to_total(self):
        """Add current score to the total score and reset current score."""
        self.total_score += self.current_score
        self.current_score = 0
