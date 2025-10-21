# test_game.py
import unittest
from unittest.mock import patch
from player import Player
from dice import Dice

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Alex")
        self.name_dict = {"Alex": self.player}

    def test_add_total_score_accumulates(self):
        self.assertEqual(self.player.total_score, 0)
        self.player.add_total_score(5)
        self.player.add_total_score(7)
        self.assertEqual(self.player.total_score, 12)

    def test_reset_turn_sets_current_to_zero_and_prints(self):
        self.player.current_score = 15
        with patch("builtins.print") as mock_print:
            self.player.reset_turn()
        self.assertEqual(self.player.current_score, 0)
        mock_print.assert_called_once()

    def test_change_name_success_updates_self_and_dict(self):
        with patch("builtins.input", side_effect=["Alex", "Jordan"]), \
             patch("builtins.print") as mock_print:
            self.player.change_name(self.name_dict)

        self.assertEqual(self.player.name, "Jordan")
        self.assertIn("Jordan", self.name_dict)
        self.assertNotIn("Alex", self.name_dict)
        self.assertIs(self.name_dict["Jordan"], self.player)
        mock_print.assert_any_call("Name changed to Jordan")

    def test_change_name_not_found_prints_message(self):
        with patch("builtins.input", side_effect=["Bob", "Jordan"]), \
             patch("builtins.print") as mock_print:
            self.player.change_name(self.name_dict)

        self.assertEqual(self.player.name, "Alex")
        self.assertIn("Alex", self.name_dict)
        self.assertNotIn("Jordan", self.name_dict)
        mock_print.assert_any_call("Bob not found")

class TestDice(unittest.TestCase):
    def test_roll_in_range(self):
        d = Dice(6)
        for _ in range(200):
            r = d.roll()
            self.assertGreaterEqual(r, 1)
            self.assertLessEqual(r, 6)

    @patch("dice.random.randint", return_value=4)
    def test_roll_calls_random_with_correct_bounds(self, mock_randint):
        d = Dice(20)
        self.assertEqual(d.roll(), 4)
        mock_randint.assert_called_with(1, 20)

if __name__ == "__main__":
    unittest.main()
