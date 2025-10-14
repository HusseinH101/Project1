class Player:
    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.current_score = 0

    def reset_turn(self):
        self.current_score = 0
