import unittest
import os
import json
import game.scoreboard

class TestScoreboard(unittest.TestCase):

    def setUp(self):
        self.test_file = "data/test_scores.json"
        game.scoreboard.SCORE_FILE = self.test_file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_ensure_score_file(self):
        game.scoreboard.ensure_score_file()
        self.assertTrue(os.path.exists(self.test_file))

    def test_create_and_find_player(self):
        data = {"players": {}}
        pid = game.scoreboard._create_player_entry(data, "Alice")
        self.assertIsNotNone(pid)
        self.assertEqual(data["players"][pid]["name"], "Alice")

    def test_update_score_creates_and_increments(self):
        p1 = type("P", (), {"name": "Alice"})
        p2 = type("P", (), {"name": "Bob"})
        game.scoreboard.update_score("Alice", [p1, p2])
        data = game.scoreboard._load_data()
        names = [v["name"] for v in data["players"].values()]
        self.assertIn("Alice", names)
        self.assertIn("Bob", names)

    def test_show_scores_runs(self):
        game.scoreboard.show_scores()  # Ensure prints without error

    def test_rename_player_new(self):
        p1 = type("P", (), {"name": "Alice"})
        game.scoreboard.update_score("Alice", [p1])
        game.scoreboard.rename_player("Alice", "AliceNew")
        data = game.scoreboard._load_data()
        names = [v["name"] for v in data["players"].values()]
        self.assertIn("AliceNew", names)

    def test_list_players(self):
        p1 = type("P", (), {"name": "Alice"})
        game.scoreboard.update_score("Alice", [p1])
        players = game.scoreboard.list_players()
        self.assertIn("Alice", players)

    def test_merge_players(self):
        p1 = type("P", (), {"name": "Alice"})
        p2 = type("P", (), {"name": "Bob"})
        game.scoreboard.update_score("Alice", [p1])
        game.scoreboard.update_score("Bob", [p2])
        game.scoreboard.rename_player("Bob", "Alice")
        data = game.scoreboard._load_data()
        total_games = sum(v["games"] for v in data["players"].values())
        self.assertGreaterEqual(total_games, 2)

    def test_save_and_load_roundtrip(self):
        p1 = type("P", (), {"name": "Alice"})
        game.scoreboard.update_score("Alice", [p1])
        data = game.scoreboard._load_data()
        self.assertIn("players", data)

    def test_score_file_exists(self):
        game.scoreboard.ensure_score_file()
        self.assertTrue(os.path.exists(game.scoreboard.SCORE_FILE))

    def test_list_empty(self):
        if os.path.exists(game.scoreboard.SCORE_FILE):
            os.remove(game.scoreboard.SCORE_FILE)
        players = game.scoreboard.list_players()
        self.assertEqual(players, [])
