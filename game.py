from human import Human
from player import Player
from ai import Ai
class Game:
    def __init__(self):
        pass

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
    def amount_of_players(self):
        response= '1'
        print(input("How many players will play in this game? (1, 2) Use the number keys to enter your selection"))
        if response == '1':
            print(input("What do you choose for your first gesture?")) 

    def dominate_signs(self):
        # if player1 == "paper" and player2 == "rock":
            # print("Player 1 wins this round.")

        self.scissors > self.paper
        self.rock > self.lizard
        self.lizard > self.spock
        self.spock > self.scissors
        self.scissors > self.lizard
        self.lizard > self.paper
        self.paper > self.spock
        self.spock > self.rock
        self.rock > self.scissors



    def ai_player(self):
         ai = Ai()
         ai.choose_gesture_ai()
        


        





# Rock crushes Scissors
# Scissors cuts Paper 
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
    def run_game(self):
        self.display_greeting()
        self.display_rules()
        self.amount_of_players()    

    def game_winner(self):
        if self.human_player >= 2:
            print(f"{self.human_player} wins the game!")
        elif self.Ai_player >= 2:
            print(f"{self.Ai_player} wins the game!")