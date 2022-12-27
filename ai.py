from player import Player
import random
class Ai(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture_ai(self):
        self.ai_gesture = random.choice(Player.__init__)
        print(self.ai_gesture)
