from player import Player
import random
class Ai(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.choose_gesture = random.randrange(len(Player.gestures))