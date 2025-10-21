from player import Player
from bot import ComputerPlayer
from dice import Dice
import json
import os


class Game:
    def __init__(self):
        self.players = []
        self.dice = Dice()
        self.current_player_index = 0
        self.score_file = os.path.join('data', 'scores.json')
        self.ensure_score_file()
       
    def ensure_score_file(self):
        '''Create the score file if it doesnt exist.'''
        if not os.path.exists('data'):
            with open(self.score_file, 'W') as f:
                json.dump({}, f)
   
   
    # ----------------------------
    # MENU SECTION
    # ----------------------------
    def show_menu(self):
        while True:
            print("\n1. Play Single Player")
            print("2. Play Two Players")
            print("3. View Rules")
            print("4. Quit")
           
            choice = input("Choose an option: ")
           
            if choice == "1":
                self.start_single_player()
            elif choice == "2":
                self.start_two_player()
            elif choice == "3":
                self.show_rules()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")
     
               
    # ----------------------------
    # GAME MODES
    # ----------------------------
   
    def start_single_player(self):
        # Ask for player name
        name = input("Enter your name: ")
        human = Player(name)
        computer = ComputerPlayer("Computer", intelligence='normal')
        self.players = [human, computer]
        self.play_game()
        print(f"Starting game: {human.name} vs {computer.name}")
        # TODO: Implement turn logic
   
    def start_two_player(self):
        # Ask for player names
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        self.players = [Player(name1), Player(name2)]
        self.players = [Player(name1), Player(name2)]
        self.play_game()
       
        print(f"Starting game: {name1} vs {name2}")
        # TODO: Implement turn logic
       
       
    # ----------------------------
    # GAME LOOP
    # ----------------------------
       
       
       
       
       
       
       
       
       
       
   
    def show_rules(self):
        print("\nRules of Pig Dice Game:")
        print("1. Roll the dice, accumulating points each turn.")
        print("2. If you roll a 1, you lose your turn score.")
        print("3. You can choose to 'hold' to save your points.")
        print("4. First player to reach 100 points wins!")



