
"""User interface module for the Pig Dice Game."""

import os
import time


class UI:
    """Handle the user interface with the Pig Dice Game."""

    def clear_screen(self):
        """Clear the screen depending on the operating system."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_title(self):
        """Display the introduction to the game."""
        print("🎲 WELCOME TO THE PIG DICE GAME 🎲")

    def show_dice(self, roll):
        """Print a visual representation of the dice roll.

        Args:
            roll (int): Result of the dice toss (1-6).
        """
        dice_style = {
            1: [
                "+----------+",
                "|          |",
                "|    o     |",
                "|          |",
                "+----------+",
            ],
            2: [
                "+----------+",
                "| o        |",
                "|          |",
                "|        o |",
                "+----------+",
            ],
            3: [
                "+----------+",
                "| o        |",
                "|     o    |",
                "|        o |",
                "+----------+",
            ],
            4: [
                "+----------+",
                "| o      o |",
                "|          |",
                "| o      o |",
                "+----------+",
            ],
            5: [
                "+----------+",
                "| o      o |",
                "|     o    |",
                "| o      o |",
                "+----------+",
            ],
            6: [
                "+----------+",
                "| o  o  o  |",
                "|          |",
                "| o  o  o  |",
                "+----------+",
            ],
        }

        print("\n🎲 Dice rolled: \n")
        for line in dice_style[roll]:
            print(line)
        time.sleep(1)

    def show_scores(self, players):
        """Display a scoreboard with ANSI color styling.

        Args:
            players (list): List of player objects, each with
                            name, total_score, and current_score attributes.
        """
        print("\n\033[1;33mSCOREBOARD:\033[0m")
        print("-" * 30)
        for p in players:
            print(
                f"{p.name:<10}| Total: {p.total_score:<3} | "
                f"Current Score: {p.current_score}"
            )
        print("." * 30)

    def winner(self, winner):
        """Declare and congratulate the winner.

        Args:
            winner (object): The player object who won the Pig Dice game.
        """
        print("\n🏆 \033[1;32mCONGRATULATIONS!\033[0m 🏆")
        print(f"{winner.name} wins the game with {winner.total_score} points!")
