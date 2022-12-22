from player import Player
import random
class Ai:
    def __init__(self): -> None:
    super().__init__()

    def choose_gesture(self): -> None:
    self.chosen_gesture = random.randrange(len(Player.gestures))