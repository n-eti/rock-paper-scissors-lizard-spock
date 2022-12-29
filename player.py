class Player:
    def __init__(self):
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock" ]
        self.score = 0

    # def score_a_point(self):
    #     self.score += 1
    
    def choose_gesture(self):
        self.gesture = input('What gesture would you like to use? ')
        
        
        
        # self.choose_gesture = ''
        # self.game_score = 0
    # This is called an abstract method. We need to create the logic for this in the AI and 
    # human classes and so we have to import and instantiate player using the super().__init__()
         
    # def player_gestures(self):
    #     response = input("Rock, Paper, Scissors, Lizard, Spock? "):
    #     self.paper > self.rock
    #     self.scissors > self.paper
    #     self.rock > self.lizard
    #     self.lizard > self.spock
    #     self.spock > self.scissors
    #     self.scissors > self.lizard
    #     self.lizard > self.paper
    #     self.paper > self.spock
    #     self.spock > self.rock
    #     self.rock > self.scissors

    def winning_choice(self):
        pass