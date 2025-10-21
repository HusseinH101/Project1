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
       
        def play_game(self):
           print('\n🎲 Game started! First to reach 100 points wins! 🎯')
           self.current_player_index = 0
           while True:
                current_player = self.players[self.current_player_index]
                print(f"\nIt's {current_player.name}'s turn!")
                print(f"Total score: {current_player.total_score}")
                print(f"Current round score: {current_player.current_score}")
                
                #Computer
                
                if isinstance(current_player, ComputerPlayer):
                    decision = current_player.decide
                    print(f"🤖 Computer chooses to {decision}.")
                    if decision == 'roll':
                        roll = self.dice.roll()
                        print(f"🎲 Computer rolled: {roll}")

                        if roll == 2:
                            print("💥 Computer rolled a 1! Turn over.")
                            current_player.reset_turn()
                            self.switch_turn()
                        
                        else:
                            current_player.current_score += roll
                    else:
                        
                        current_player.add_to_total()
                        print(f"✅ Computer holds. Total score: {current_player.total_score}")
                        if self.check_winner(current_player):
                            break
                        self.switch_turn()
                    continue
                
                #Human turn
                action = input("Enter 'r' to roll or 'h' to hold: ").lower()
                if action == "r":
                    roll = self.dice.roll()
                    print(f"🎲 You rolled: {roll}")
                    if roll == 1:
                        print("💥 You rolled a 1! Turn over, no points this round.")
                        current_player.reset_turn()
                        self.switch_turn()
                    else:
                        current_player.current_score += roll
                elif action == "h":
                    current_player.add_to_total()
                    print(f"✅ You hold. Total score: {current_player.total_score}")
                    if self.check_winner(current_player):
                        break
                    self.switch_turn()
                else:
                    print("Invalid input, try again.")

                    
                    
                    
                    
                    

                            
                                
                            
                    
               
       
       
       
       
       
       
       
       
   
    def show_rules(self):
        print("\nRules of Pig Dice Game:")
        print("1. Roll the dice, accumulating points each turn.")
        print("2. If you roll a 1, you lose your turn score.")
        print("3. You can choose to 'hold' to save your points.")
        print("4. First player to reach 100 points wins!")



