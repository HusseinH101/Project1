import unittest
from game.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Alice")

    def test_initial_values(self):
        self.assertEqual(self.player.name, "Alice")
        self.assertEqual(self.player.total_score, 0)
        self.assertEqual(self.player.current_score, 0)
        self.assertIsInstance(self.player.name, str)
        self.assertIsInstance(self.player.total_score, int)
        self.assertIsInstance(self.player.current_score, int)
        self.assertGreaterEqual(self.player.total_score, 0)
        self.assertGreaterEqual(self.player.current_score, 0)

    def test_add_to_total(self):
        self.player.current_score = 5
        self.player.add_to_total()
        self.assertEqual(self.player.total_score, 5)
        self.assertEqual(self.player.current_score, 0)
        self.player.current_score = 3
        self.player.add_to_total()
        self.assertEqual(self.player.total_score, 8)
        self.assertEqual(self.player.current_score, 0)

    def test_reset_turn(self):
        self.player.current_score = 7
        self.player.reset_turn()
        self.assertEqual(self.player.current_score, 0)
        self.assertEqual(self.player.total_score, 0)

    def test_multiple_turns_accumulate(self):
        self.player.current_score = 4
        self.player.add_to_total()
        self.player.current_score = 6
        self.player.add_to_total()
        self.assertEqual(self.player.total_score, 10)
        self.assertEqual(self.player.current_score, 0)

    def test_no_negative_total(self):
        self.player.add_to_total()
        self.assertGreaterEqual(self.player.total_score, 0)
        self.assertGreaterEqual(self.player.current_score, 0)

    def test_name_is_string(self):
        self.assertIsInstance(self.player.name, str)
        self.assertEqual(self.player.name, "Alice")

    def test_reset_multiple_times(self):
        self.player.current_score = 10
        self.player.reset_turn()
        self.player.reset_turn()
        self.assertEqual(self.player.current_score, 0)

    def test_add_after_reset(self):
        self.player.current_score = 5
        self.player.reset_turn()
        self.player.add_to_total()
        self.assertEqual(self.player.total_score, 0)
        self.assertEqual(self.player.current_score, 0)

    def test_state_combination(self):
        self.player.current_score = 3
        self.player.add_to_total()
        self.player.reset_turn()
        self.assertEqual(self.player.total_score, 3)
        self.assertEqual(self.player.current_score, 0)

    def test_types(self):
        self.assertIsInstance(self.player.total_score, int)
        self.assertIsInstance(self.player.current_score, int)
