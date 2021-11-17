import random

from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()
        self.set_name()
        
    def hand_gesture(self):
        self.choice = random.choice(self.gesture_list) #the choice list goes here>
        if self.choice == "Rock":
           print(f'Player 2 selected {self.choice}')
        elif self.choice == "Paper":
           print(f'Player 2 selected {self.choice}')
        elif self.choice == "Scissors":
           print(f'Player 2 selected {self.choice}')
        elif self.choice == "Lizard":
           print(f'Player 2 selected {self.choice}')
        elif self.choice == "Spock":
           print(f'Player 2 selected {self.choice}')

    def set_name(self):
        self.name = "Master AI"