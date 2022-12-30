from human import Human
from ai import Ai
from game import Game

player = Game()

player.choose_gestures()
player.compare_gestures()
print()
player.keep_score()
print()