from player import Player
import random
class Ai:
    def __init__(Player): -> None:
        super().__init__(Player)

    def choose_gesture(self): -> None:
        self.chosen_gesture = random.randrange(len(Player.gestures))