from human import Human
from ai_player import AI
from player import Player

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None

    def create_gesture(self):
        pass

    def welcome(self):
        print("\n *** Welcome to \"Rock, Paper, Scissors, Lizzard, Spock\" The Game ***\n")
        new_game = input("Ready to begin the game? Yes or No: ").lower()
        if new_game == "yes":
            return True
        else:
            return False

    def run_game(self):
        start_game = self.welcome()
        if start_game == True:
            self.player_name()
            mode_game = self.game_mode()
            if mode_game == 1:
                self.rules()
                self.gameplay()
            else:
                self.rules()
                self.gameplay_human()
            #self.player_one.hand_gesture()
            #self.player_two.hand_gesture()
            #self.define_win()
            #self.display_winner()
      

    def gameplay(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            self.player_one.choose_gesture()
            self.player_two.hand_gesture()
            self.define_win()
        self.display_winner()
        print(input("\nPress ENTER to continue..."))
        self.run_game()

    def gameplay_human(self):
            while self.player_one.score < 2 and self.player_two.score < 2:
                self.player_one.choose_gesture()
                self.player_two.choose_gesture()
                self.define_win()
            self.display_winner()
            print(input("\nPress ENTER to continue..."))
            self.run_game()



    def rules(self):
        print(f"\nLet THE GAME BEGIN\n\n{self.player_one.name} vs. {self.player_two.name}\n*To play*\nEach player chooses one gesture from the list:")
        print("For each players gesture chosen;\n")
        print("Rock crushes Scissors\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock")
        print("\nIf the same gestures are played, round results in a tie and must be replayed immediately.")
        print("There can only be one winner per round.\nThe player who wins best out of three will be the champion.")
        print(input("\nPress ENTER to continue..."))

    def game_mode(self):
        print("\nSelect GAMEMODE\nSingle Player or Multi-Player?")
        mode = int(input("\nType \"1\" for Single Player or \"2\" for Multi-Player: "))
        if mode == 2:
            self.player_two = Human(input("Enter a name for the second player: "))
            print(f"{self.player_two.name} is player two.")
            print(input("\nPress ENTER to continue..."))
            return mode
        else:
            self.player_two = AI()
            print(f"{self.player_two.name} is player two.")
            print(input("\nPress ENTER to continue..."))
            return mode

    def player_name(self):
        self.player_one = Human(input("Enter a name for the first player: "))
        print(f"{self.player_one.name} is player one.")
        print(input("\nPress ENTER to continue..."))


# dependant on 1 or 2 player we need to start a player vs player game or player vs ai game.
# single player will take user input to select a gesture and compare it to the AI randon gesture.
# two player will take both user inputs and compare them together. 
# both need to identify a tie then replay.
# both need to identify a winning gesture selection
# when a player gets the round win it gets added to a win counter.
# The win counter has to be best out of three.
    #when players win count when compared to the other player is > 2 they win.

    def define_win(self):
        if self.player_one.choice == self.player_two.choice:
            print(f"Both players selected {self.player_one.choice}. You tied.")
        elif self.player_one.choice == "Rock" :
            if self.player_two.choice == "Scissors" or self.player_two.choice == "Lizard":
                print(f"{self.player_one.choice} crushes {self.player_two.choice}, {self.player_one.name} wins this round")
                self.player_one.score += 1
            elif self.player_two.choice == "Spock" or self.player_two.choice == "Paper":
                print(f"{self.player_two.choice} vaporizes {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1  
        elif self.player_one.choice == "Paper":
            if self.player_two.choice == "Rock" or self.player_two.choice == "Spock":
                print(f"{self.player_one.choice} covers {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "Lizard" or self.player_two.choice == "Scissors":
                print(f"{self.player_two.choice} eats {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        elif self.player_one.choice == "Scissors":
            if self.player_two.choice == "Paper" or self.player_two.choice == "Lizard":
                print(f"{self.player_one.choice} cuts {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "Spock" or self.player_two.choice == "Rock":
                print(f"{self.player_two.choice} smashes {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        elif self.player_one.choice == "Lizard":
            if self.player_two.choice == "Spock" or self.player_two.choice == "Paper":
                print(f"{self.player_one.choice} poisons {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "Rock" or self.player_two.choice == "Scissors":
                print(f"{self.player_two.choice} crushes {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1
        elif self.player_one.choice == "Spock":
            if self.player_two.choice == "Scissors" or self.player_two.choice == "Rock":
                print(f"{self.player_one.choice} smashes {self.player_two.choice}! {self.player_one.name} wins this round!")
                self.player_one.score += 1
            elif self.player_two.choice == "Paper" or self.player_two.choice == "Lizard":
                print(f"{self.player_two.choice} disaproves {self.player_one.choice}! {self.player_two.name} wins this round.")
                self.player_two.score += 1 
    
    def display_winner(self): #if a players score is 2 higher then the others that player wins
        if self.player_one.score == 2: 
            print(f"{self.player_one.name} Wins the game!")
        else:
            print(f"{self.player_two.name} Wins the game!")

