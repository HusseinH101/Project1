import unittest
from game import Game
from game.player import Player
from game.bot import ComputerPlayer

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.p1 = Player("Alice")
        self.p2 = ComputerPlayer("Bot", intelligence="easy")
        self.game.players = [self.p1, self.p2]

    def test_switch_turn(self):
        self.assertEqual(self.game.current_player_index, 0)
        self.game.switch_turn()
        self.assertEqual(self.game.current_player_index, 1)
        self.game.switch_turn()
        self.assertEqual(self.game.current_player_index, 0)

    def test_roll_dice(self):
        val = self.game.roll_dice()
        self.assertIn(val, range(1, 7))
        self.assertEqual(self.game.roll_dice(cheat_number=6), 6)

    def test_play_bot_turn_roll(self):
        self.p2.current_score = 0
        self.game.play_bot_turn()
        self.assertGreaterEqual(self.p2.current_score, 0)
        self.assertLessEqual(self.p2.current_score, 6)

    def test_get_winner_none(self):
        self.assertIsNone(self.game.get_winner())

    def test_get_winner_found(self):
        self.p1.total_score = 100
        self.assertEqual(self.game.get_winner().name, "Alice")

    def test_reset_game(self):
        self.p1.total_score = 50
        self.p1.current_score = 20
        self.game.reset()
        self.assertEqual(self.p1.total_score, 0)
        self.assertEqual(self.p1.current_score, 0)
        self.assertEqual(self.game.current_player_index, 0)

    def test_check_winner_true_false(self):
        self.p1.total_score = 99
        self.assertFalse(self.game.check_winner(self.p1))
        self.p1.total_score = 100
        self.assertTrue(self.game.check_winner(self.p1))

    def test_switch_turn_cycle(self):
        self.game.current_player_index = 1
        self.game.switch_turn()
        self.assertEqual(self.game.current_player_index, 0)

    def test_play_bot_turn_hold(self):
        self.p2.intelligence = "hard"
        self.p2.current_score = 40
        self.game.play_bot_turn()
        self.assertEqual(self.p2.current_score, 0)

    def test_print_status_runs(self):
        self.game._print_status()  # Just ensure no crash
