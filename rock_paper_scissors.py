import os 
from time import sleep
from random import randint

class RockPaperScissors():

    def __init__(self, computer, player, game_status): 
        self.computer = computer
        self.player = player
        self.game_status = game_status
        self.game_status = {
            'playing': False
        }
        
    def users_turn(self):
        self.user = input("\nChoose between rock, paper, and scissors. Type r / p / s\n")
        os.system('clear')
        if self.user.lower() == "r":
            print("\n\tYour choice: Rock")
            pass
        elif self.user.lower() == "p":
            print("\n\tYour choice: Paper")
            pass
        elif self.user.lower() == "s":
            print("\n\tYour choice: Scissors")
            pass
        else:
            print("\n\tInvalid input. Please try again.\n")
            self.users_turn()

    
    def computers_turn(self):
        self.computer = randint(1, 3)
        if self.computer == 1:
            print("\n\tComputer's choice: Rock\n")
        elif self.computer == 2:
            print("\n\tComputer's choice: Paper\n")
        elif self.computer == 3:
            print("\n\tComputer's choice: Scissors\n")

    def determine_winner(self):
        if self.computer == 1:   # rock
            if self.user == "r":
                print("\tIt's a tie! You both chose Rock\n")
            elif self.user == "p":
                print("\tPaper covers rock. You win!\n")
            elif self.user == "s":
                print("\tRock crushes scissor. Computer wins.\n")
        elif self.computer == 2:     # paper
            if self.user == "p":   
                print("\tIt's a tie! You both chose Paper\n")
            elif self.user == "r":
                print("\tPaper covers rock. Computer wins.\n")
            elif self.user == "s":
                print("\tScissors cut paper. You win!\n")
        elif self.computer == 3:  # scissors
            if self.user == "s":
                print("\tIt's a tie! You both chose Scissors\n")
            elif self.user == "r":
                print("\tRock crushes scissors. You win!\n")
            elif self.user == "p":
                print("\tScissors cut paper. Computer wins.\n")
    
    def keep_playing(self):
        ask = input("Would you like to play again? y/n\n")
        if ask.lower() == "y":
            self.game_status['playing'] = True
            os.system('clear')
        elif ask.lower() == "n":
            self.game_status['playing'] = False
            os.system('clear')
            print("Thanks for playing!")



play = RockPaperScissors("Computer", "Player", {})

def run():
    play.game_status['playing'] = True
    while play.game_status['playing'] == True:
        print("\nWelcome to Rock, Paper, Scissors! Let's play!\n\t")
        sleep(3)
        os.system('clear')
        play.users_turn()
        play.computers_turn()
        play.determine_winner()
        play.keep_playing()

run()