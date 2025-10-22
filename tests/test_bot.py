"""Unit tests for the ComputerPlayer class in the Pig Dice Game."""

import unittest
from bot import ComputerPlayer  # Rätt import här


class TestComputerPlayer(unittest.TestCase):
    """Test cases for the ComputerPlayer class."""

    def setUp(self):
        """Set up test data for the ComputerPlayer class."""
        self.easy_bot = ComputerPlayer("EasyBot", intelligence="easy")
        self.normal_bot = ComputerPlayer("NormalBot", intelligence="normal")
        self.hard_bot = ComputerPlayer("HardBot", intelligence="hard")

    def test_initialization(self):
        """Test initialization of ComputerPlayer objects."""
        self.assertEqual(self.easy_bot.name, "EasyBot")
        self.assertEqual(self.normal_bot.name, "NormalBot")
        self.assertEqual(self.hard_bot.name, "HardBot")
        self.assertEqual(self.easy_bot.intelligence, "easy")
        self.assertEqual(self.normal_bot.intelligence, "normal")
        self.assertEqual(self.hard_bot.intelligence, "hard")

    def test_decide_easy_random_output(self):
        """Test easy level decision (random roll or hold)."""
        results = set()
        for _ in range(100):  # Test multiple times to capture randomness
            results.add(self.easy_bot.decide())
        self.assertIn("roll", results)
        self.assertIn("hold", results)

    def test_decide_normal_below_20(self):
        """Test normal difficulty where score is less than 20."""
        self.normal_bot.current_score = 10
        decision = self.normal_bot.decide()
        self.assertEqual(decision, "roll")

    def test_decide_normal_at_20(self):
        """Test normal difficulty where score is exactly 20."""
        self.normal_bot.current_score = 20
        decision = self.normal_bot.decide()
        self.assertEqual(decision, "hold")

    def test_decide_normal_above_20(self):
        """Test normal difficulty where score is above 20."""
        self.normal_bot.current_score = 25
        decision = self.normal_bot.decide()
        self.assertEqual(decision, "hold")

    def test_decide_hard_total_score_approaching_100(self):
        """Test hard difficulty when the total score is near 100."""
        self.hard_bot.total_score = 95
        self.hard_bot.current_score = 5
        decision = self.hard_bot.decide()
        self.assertEqual(decision, "hold")

    def test_decide_hard_high_current_score(self):
        """Test hard difficulty when current score is high enough to hold."""
        self.hard_bot.current_score = 30
        decision = self.hard_bot.decide()
        self.assertEqual(decision, "hold")

    def test_decide_hard_roll_below_100(self):
        """Test hard difficulty when total score is not enough to hold."""
        self.hard_bot.total_score = 40
        self.hard_bot.current_score = 10
        decision = self.hard_bot.decide()
        self.assertEqual(decision, "roll")

    def test_case_insensitive_intelligence(self):
        """Test that the intelligence level is case-insensitive."""
        bot = ComputerPlayer("MixedCaseBot", intelligence="NoRmAl")
        self.assertEqual(bot.intelligence, "normal")
        bot.current_score = 21
        self.assertEqual(bot.decide(), "hold")


if __name__ == "__main__":
    unittest.main()
