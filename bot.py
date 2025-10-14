from player import Player
import random

class ComputerPlayer(Player):
    def __init__(self, name, intelligence="normal"):
        super().__init__(name)
        self.intelligence = intelligence

    def decide(self):
        # You can later make this smarter (AI)
        if self.intelligence == "easy":
            return random.choice(["roll", "hold"])
        elif self.intelligence == "normal":
            return "hold" if self.current_score >= 20 else "roll"
        else:
            return "hold" if self.current_score >= 10 else "roll"
