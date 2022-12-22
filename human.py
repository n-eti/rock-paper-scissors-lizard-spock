from player import Player

class Human:
    def __init__(self, Player):
        super().__init__(Player)

    

    def choose_gesture(self):
        response = input(f"Choose your gesture: 0 = {0}, 1 = {1}, 2 = {2}, 3 = {3}, or 4 = {4}")

    def round_score(self):
        self.