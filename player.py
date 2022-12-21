class Player:
    def __init__(self, player_1, player_2, player_3):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_3 = player_3

    def how_many_players(self):
        input("How many players will play in this game? 1, 2, or 3 ")
    
    def player_gestures(self):
        response = input("Rock, Paper, Scissors, Lizard, Spock? ")

    def winning_choice(self):
        pass