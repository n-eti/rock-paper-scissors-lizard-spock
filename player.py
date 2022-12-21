class Player:
    def __init__(self, player_1, player_2, player_3, rock, paper, scissors, lizard, spock):
        self.player_1 = player_1
        self.player_2 = player_2
        self.player_3 = player_3
        self.rock = rock
        self.scissors = scissors
        self.paper = paper
        self.lizard = lizard
        self.spock = spock


    def how_many_players(self):
        input("How many players will play in this game? 1, 2, or 3 ")
    
    def player_gestures(self):
        # response = input("Rock, Paper, Scissors, Lizard, Spock? "):
        self.paper > self.rock
        self.scissors > self.paper
        self.rock > self.lizard
        self.lizard > self.spock
        self.spock > self.scissors
        self.scissors > self.lizard
        self.lizard > self.paper
        self.paper > self.spock
        self.spock > self.rock
        self.rock > self.scissors
        




    def winning_choice(self):
        pass