from player import Player
import random
class Ai(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture_ai(self):
        possible_actions = ["rock", "paper", "scissors", "spok", "lizard" ]
        self.choosen_gesture = random.choice(possible_actions)
        print(self.choosen_gesture)
