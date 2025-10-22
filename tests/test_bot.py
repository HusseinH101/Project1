import unittest
from unittest.mock import patch
from bot import ComputerPlayer

class TestComputerPlayer(unittest.TestCase):
    """class for testing the intelligence of the computer"""
    def setUp(self):
        self.easy_bot = ComputerPlayer("EasyBot", intelligence="easy")
        self.normal_bot = ComputerPlayer("NormalBot", intelligence="normal")
        self.hard_bot = ComputerPlayer("HardBot", intelligence="hard")

    @patch('random.choice', return_value="roll")
    def test_easy_bot_returns_random_choice(self, mock_choice):
        result = self.easy_bot.decide()
        self.assertEqual(result, "roll")
        mock_choice.assert_called_once_with(["roll", "hold"])

    def test_normal_bot_rolls_under_20(self):
        self.normal_bot.current_score = 15
        self.assertEqual(self.normal_bot.decide(), "roll")
    
    def test_normal_bot_holds_at_20_or_more(self):
        self.normal_bot.current_score = 20
        self.assertEqual(self.normal_bot.decide(), "hold")

    def test_hard_bot_holds_when_total_plus_current_reaches_100(self):
        self.hard_bot.total_score = 90
        self.hard_bot.current_score = 15
        self.assertEqual(self.hard_bot.decide(), "hold")

    
    def test_hard_bot_holds_rolls_otherwise(self):
        self.hard_bot.total_score = 50
        self.hard_bot.current_score = 10
        self.assertEqual(self.hard_bot.decide(), "roll")

    def test_hard_bot_if_current_score_25(self):
        self.hard_bot.current_score = 25
        self.hard_bot.total_score = 20
        self.assertEqual(self.hard_bot.decide(), "hold")

    def test_intelligence_is_lowercased(self):
        self.hard_bot = ComputerPlayer("Hardbot", intelligence="HARD")
        self.hard_bot.current_score = 30
        self.assertEqual(self.hard_bot.decide(), "hold")

    def test_invalid_intelligence_still_roll(self):
        self.normal_bot = ComputerPlayer("normalbot", intelligence="Unknown")
        self.normal_bot.current_score = 10
        self.normal_bot.total_score = 20
        self.assertEqual(self.normal_bot.decide(), "roll")

    def test_default_intelligence_is_normal(self):
        self.easy_bot = ComputerPlayer("easybot")
        self.easy_bot.current_score = 10
        self.assertEqual(self.easy_bot.decide(), "roll")
    
    def test_bot_for_holding_on_25_plus(self):
        self.hard_bot = ComputerPlayer("hardbot", intelligence="hard")
        self.hard_bot.current_score = 26
        self.hard_bot.total_score_score = 10
        self.assertEqual(self.hard_bot.decide(), "hold")
    

if __name__=='__main__':
    unittest.main()