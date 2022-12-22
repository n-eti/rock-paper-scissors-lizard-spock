from human import Human
from player import Player
from ai import Ai

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
        self.player1 = Human()
        self.player2 = Ai()

    def display_greeting(self):
    
        print("Welcome to Rock Paper Scissors Lizard Spock.")
        print("Each match will be best of three games!")

        

    def display_rules(self):
        print (f'''
Rock crushes Scissors
Scissors cuts Paper 
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
''')
    def select_player_type(self):
        response = input("How many players will play in this game? (1, 2) Use the number keys to enter your selection ")
        if response == "2":
            self.player2 = Human()         
            # print("Use the number keys to enter your selection")
        # response = "1"
        # # if response  "1":
            

        # if response == "1":
        #     print(input("What do you choose for your first gesture?"))
            

    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.select_player_type()    

    def game_winner(self):
        if self.human_player >= 2:
            print(f"{self.human_player} wins the game!")
        elif self.Ai_player >= 2:
            print(f"{self.Ai_player} wins the game!")