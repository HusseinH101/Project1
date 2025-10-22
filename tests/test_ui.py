"""Unit tests for the UI module in the Pig Dice Game."""

import unittest
from io import StringIO
from unittest.mock import patch
from ui import UI


class DummyPlayer:
    """A simple dummy player for UI test purposes."""

    def __init__(self, name, total, current):
        """Create a DummyPlayer with name, total score, and current score."""
        self.name = name
        self.total_score = total
        self.current_score = current


class TestUI(unittest.TestCase):
    """Test cases for the UI class."""

    def setUp(self):
        """Create a UI instance and dummy players for tests."""
        self.ui = UI()
        self.players = [
            DummyPlayer("Jeyson", 80, 10),
            DummyPlayer("Hussein", 65, 5)
        ]

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_1(self, mock_stdout):
        """Test dice face for roll 1 is shown correctly."""
        self.ui.show_dice(1)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_2(self, mock_stdout):
        """Test dice face for roll 2 is shown correctly."""
        self.ui.show_dice(2)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_3(self, mock_stdout):
        """Test dice face for roll 3 is shown correctly."""
        self.ui.show_dice(3)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_4(self, mock_stdout):
        """Test dice face for roll 4 is shown correctly."""
        self.ui.show_dice(4)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_5(self, mock_stdout):
        """Test dice face for roll 5 is shown correctly."""
        self.ui.show_dice(5)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_dice_6(self, mock_stdout):
        """Test dice face for roll 6 is shown correctly."""
        self.ui.show_dice(6)
        output = mock_stdout.getvalue()
        self.assertIn("+----------+", output)
        self.assertIn("o", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_scores_prints_scoreboard(self, mock_stdout):
        """Test show_scores prints the scoreboard with correct data."""
        self.ui.show_scores(self.players)
        output = mock_stdout.getvalue()
        self.assertIn("SCOREBOARD", output)
        self.assertIn("Jeyson", output)
        self.assertIn("Hussein", output)
        self.assertIn("80", output)
        self.assertIn("65", output)
        self.assertIn("10", output)
        self.assertIn("5", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_winner_prints_congratulations(self, mock_stdout):
        """Test winner prints the congratulation message correctly."""
        self.ui.winner(self.players[0])
        output = mock_stdout.getvalue()
        self.assertIn("CONGRATULATIONS", output)
        self.assertIn("Jeyson", output)
        self.assertIn("80", output)

    def test_dummy_player_attributes(self):
        """Test attributes of the DummyPlayer."""
        player = DummyPlayer("Test", 55, 12)
        self.assertEqual(player.name, "Test")
        self.assertEqual(player.total_score, 55)
        self.assertEqual(player.current_score, 12)

    def test_ui_instance_creation(self):
        """Test UI instance is created correctly."""
        self.assertIsInstance(self.ui, UI)
