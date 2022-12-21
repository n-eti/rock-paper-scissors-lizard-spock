# Welcome to Rock Paper Scissors Lizard Spock.

# each match will be best of three games


# Scissors cuts paper 
# paper covers rock 
# rock crushes lizard 
# lizard poisons Spock 
# Spock smashes scissors 
# scissors decapitates lizard 
# lizard eats paper 
# paper disproves Spock 
# Spock vaporizes rock 
# Rock crushes scissors.


# Use the number keys to enter your selection



class Game:
    def __init__(self):
        pass

    def display_greeting(self):
        print()
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print("each match will be best of three games")
        print()

    def display_rules(self):
        print("Scissors cuts paper ")
        print("paper covers rock ")
        print("rock crushes lizard ")
        print("lizard poisons Spock  ")
        print("Spock smashes scissors  ")
        print("scissors decapitates lizard  ")
        print("lizard eats paper ")
        print("paper disproves Spock ")
        print("Spock vaporizes rock  ")
        print("Rock crushes scissors ")
        print()
        print("Use the number keys to enter your selection")

    def display_game_type(self):
        input("How many players will play in this game?")