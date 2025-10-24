import unittest
from game.bot import ComputerPlayer

class TestComputerPlayer(unittest.TestCase):

    def setUp(self):
        self.bot = ComputerPlayer("Bot", intelligence="normal")

    def test_initial_values(self):
        self.assertEqual(self.bot.name, "Bot")
        self.assertEqual(self.bot.total_score, 0)
        self.assertEqual(self.bot.current_score, 0)
        self.assertEqual(self.bot.intelligence, "normal")

    def test_reset_turn(self):
        self.bot.current_score = 10
        self.bot.reset_turn()
        self.assertEqual(self.bot.current_score, 0)

    def test_add_to_total_accumulates(self):
        self.bot.current_score = 5
        self.bot.add_to_total()
        self.assertEqual(self.bot.total_score, 5)
        self.assertEqual(self.bot.current_score, 0)

    def test_multiple_calls_stable(self):
        self.bot.current_score = 3
        self.bot.add_to_total()
        self.bot.add_to_total()
        self.assertEqual(self.bot.total_score, 3)
        self.assertEqual(self.bot.current_score, 0)

    def test_decide_easy(self):
        easy_bot = ComputerPlayer("Easy", intelligence="easy")
        decisions = [easy_bot.decide() for _ in range(20)]
        self.assertTrue(all(d in ["roll", "hold"] for d in decisions))

    def test_decide_normal_threshold(self):
        self.bot.current_score = 19
        self.assertEqual(self.bot.decide(), "roll")
        self.bot.current_score = 20
        self.assertEqual(self.bot.decide(), "hold")

    def test_decide_hard_threshold(self):
        hard_bot = ComputerPlayer("Hard", intelligence="hard")
        hard_bot.current_score = 29
        self.assertEqual(hard_bot.decide(), "roll")
        hard_bot.current_score = 30
        self.assertEqual(hard_bot.decide(), "hold")

    def test_name_string(self):
        self.assertIsInstance(self.bot.name, str)

    def test_add_and_reset_sequence(self):
        self.bot.current_score = 7
        self.bot.add_to_total()
        self.assertEqual(self.bot.total_score, 7)
        self.bot.reset_turn()
        self.assertEqual(self.bot.current_score, 0)

    def test_multiple_rolls_behavior(self):
        self.bot.current_score = 10
        self.bot.add_to_total()
        self.bot.current_score = 5
        self.assertEqual(self.bot.total_score, 10)
        self.assertEqual(self.bot.current_score, 5)
