"""
game.py
--------
Main Pig Dice Game logic.
"""

from player import Player
from bot import ComputerPlayer
from dice import Dice
import scoreboard


class Game:
    """Main class for Pig Dice Game handling setup, gameplay, and menu."""

    def __init__(self):
        self.players = []
        self.dice = Dice()
        self.current_player_index = 0

    # ----------------------------
    # MENU
    # ----------------------------
    def show_menu(self):
        """Display the game menu and handle user choices."""
        while True:
            print("\n🐷 Pig Dice Game Menu 🐷")
            print("1. Single Player")
            print("2. Two Players")
            print("3. Show Rules")
            print("4. Show High Scores")
            print("5. Quit")
            print("6. Change Player Name")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.start_single_player()
            elif choice == "2":
                self.start_two_player()
            elif choice == "3":
                self.show_rules()
            elif choice == "4":
                scoreboard.show_scores()
            elif choice == "5":
                print("Goodbye!")
                break
            elif choice == "6":
                self.change_player_name()
            else:
                print("Invalid choice, try again.")

    # ----------------------------
    # PLAYER SETUP
    # ----------------------------
    def start_single_player(self):
        """Initialize a single-player game against a computer."""
        name = input("Enter your name: ").strip()
        while True:
            lvl = input("Choose computer intelligence (easy, normal, hard) [normal]: ").strip().lower()
            if lvl == "":
                lvl = "normal"
            if lvl in ("easy", "normal", "hard"):
                break
            print("Invalid level, choose easy, normal, or hard.")
        human = Player(name)
        computer = ComputerPlayer("Computer", intelligence=lvl)
        self.players = [human, computer]
        print(f"Starting game: {human.name} vs {computer.name} ({lvl})")
        self.play_game()

    def start_two_player(self):
        """Initialize a two-player game with player names."""
        name1 = input("Enter Player 1 name: ").strip()
        name2 = input("Enter Player 2 name: ").strip()
        self.players = [Player(name1), Player(name2)]
        print(f"Starting game: {name1} vs {name2}")
        self.play_game()

    # ----------------------------
    # CHANGE PLAYER NAME
    # ----------------------------
    def change_player_name(self):
        """Allow user to change a player's name and migrate scores."""
        players = scoreboard.list_players()
        if not players:
            print("No players in scoreboard to rename.")
            return

        print("\nCurrent players in scoreboard:")
        for i, name in enumerate(players, start=1):
            print(f"{i}. {name}")

        old = input("Enter current player name to change (exact): ").strip()
        if not old or old not in players:
            print(f"Invalid input. Player '{old}' does not exist.")
            return

        new = input("Enter new name: ").strip()
        if not new:
            print("Invalid input.")
            return

        scoreboard.rename_player(old, new)
        print(f"Renamed/migrated stats from '{old}' -> '{new}'.")

            
            

        scoreboard.rename_player(old, new)
        print(f"Renamed/migrated stats from '{old}' -> '{new}'.")

    # ----------------------------
    # RULES
    # ----------------------------
    def show_rules(self):
        """Display the game rules."""
        print("\n📜 Rules of Pig Dice Game:")
        print("1. Roll the dice and collect points each turn.")
        print("2. If you roll a 1, you lose your current turn points.")
        print("3. You can hold to save your points and end your turn.")
        print("4. First to reach 100 points wins!\n")

    # ----------------------------
    # GAME LOOP
    # ----------------------------
    def play_game(self):
        """Main game loop handling turns and actions."""
        self.current_player_index = 0

        while True:
            current = self.players[self.current_player_index]
            self._print_status()
            print(f"\n{current.name}'s turn: total={current.total_score}, current={current.current_score}")

            if isinstance(current, ComputerPlayer):
                decision = current.decide()
                print(f"🤖 Computer chooses to {decision}")
                if decision == "roll":
                    roll = self.dice.roll()
                    print(f"Computer rolled: {roll}")
                    if roll == 1:
                        current.reset_turn()
                        self.switch_turn()
                    else:
                        current.current_score += roll
                else:
                    current.add_to_total()
                    if self.check_winner(current):
                        return
                    self.switch_turn()
                continue

            # Human player turn
            while True:
                action = input("Enter 'r' to roll, 'h' to hold, 'c' to cheat (auto-roll 6), or 'q' to quit: ").strip().lower()
                if action not in ("r", "h", "c", "q"):
                    print("Invalid input, try again.")
                    continue
                break

            if action == "r":
                roll = self.dice.roll()
                print(f"You rolled: {roll}")
                if roll == 1:
                    print("💥 You rolled a 1! Turn over, no points this round.")
                    current.reset_turn()
                    self.switch_turn()
                else:
                    current.current_score += roll

            elif action == "h":
                current.add_to_total()
                if self.check_winner(current):
                    return
                self.switch_turn()

            elif action == "c":
                roll = self.dice.roll(cheat_number=6)
                print("😈 Cheat activated! You rolled a 6!")
                current.current_score += roll

            elif action == "q":
                print("Quitting current game and returning to menu.")
                for p in self.players:
                    p.current_score = 0
                return

    # ----------------------------
    # TURN & WIN LOGIC
    # ----------------------------
    def switch_turn(self):
        """Switch to next player."""
        if not self.players:
            return
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def check_winner(self, player):
        """Check win condition and update scoreboard."""
        if player.total_score >= 100:
            print(f"\n🏆 {player.name} wins with {player.total_score} points! 🏆")
            scoreboard.update_score(player.name, self.players)
            return True
        return False

    # ----------------------------
    # DISPLAY HELPERS
    # ----------------------------
    def _print_status(self):
        """Print a coarse progress bar (out of 10) based on total + current turn points.

        Uses total + current so a player who has accumulated points in the current
        turn sees the progress immediately (e.g. after cheating)."""
        parts = []
        for p in self.players:
            total = getattr(p, "total_score", 0)
            current = getattr(p, "current_score", 0)
            progress = min(total + current, 100)  # cap at 100
            filled = progress // 10                # 0..10 blocks
            bar = "█" * filled
            parts.append(f"{p.name}: [{bar:<10}] {total}pts (+{current})")
        if parts:
            print("\n" + " | ".join(parts))