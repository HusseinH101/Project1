# test_scoreboard.py
import unittest
from unittest.mock import patch
import tempfile
import os
import json
import sys

# Add parent folder to path so we can import scoreboard
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import scoreboard

class TestScoreboard(unittest.TestCase):
    def setUp(self):
        # Temporary directory for scores.json
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_score_file = scoreboard.SCORE_FILE
        scoreboard.SCORE_FILE = os.path.join(self.temp_dir.name, "scores.json")

    def tearDown(self):
        self.temp_dir.cleanup()
        scoreboard.SCORE_FILE = self.original_score_file

    # -------------------------
    # ensure_score_file
    # -------------------------
    def test_ensure_score_file_creates_file_and_folder(self):
        self.assertFalse(os.path.exists(scoreboard.SCORE_FILE))
        scoreboard.ensure_score_file()
        self.assertTrue(os.path.exists(scoreboard.SCORE_FILE))
        self.assertTrue(os.path.exists(os.path.dirname(scoreboard.SCORE_FILE)))

    def test_ensure_score_file_idempotent(self):
        scoreboard.ensure_score_file()
        with open(scoreboard.SCORE_FILE) as f:
            data_before = f.read()
        scoreboard.ensure_score_file()
        with open(scoreboard.SCORE_FILE) as f:
            data_after = f.read()
        self.assertEqual(data_before, data_after)

    # -------------------------
    # update_score
    # -------------------------
    def test_update_score_creates_entries(self):
        from types import SimpleNamespace
        players = [SimpleNamespace(name="Alice", total_score=100),
                   SimpleNamespace(name="Bob", total_score=50)]
        scoreboard.update_score("Alice", players)
        with open(scoreboard.SCORE_FILE) as f:
            data = json.load(f)
        self.assertIn("players", data)
        names = [p["name"] for p in data["players"].values()]
        self.assertIn("Alice", names)
        self.assertIn("Bob", names)

    def test_update_score_counts_wins_and_losses(self):
        from types import SimpleNamespace
        players = [SimpleNamespace(name="Alice", total_score=100),
                   SimpleNamespace(name="Bob", total_score=50)]
        scoreboard.update_score("Alice", players)
        with open(scoreboard.SCORE_FILE) as f:
            data = json.load(f)
        for p in data["players"].values():
            if p["name"] == "Alice":
                self.assertEqual(p["wins"], 1)
                self.assertEqual(p["losses"], 0)
                self.assertEqual(p["games"], 1)
            elif p["name"] == "Bob":
                self.assertEqual(p["wins"], 0)
                self.assertEqual(p["losses"], 1)
                self.assertEqual(p["games"], 1)

    def test_update_score_multiple_updates(self):
        from types import SimpleNamespace
        players = [SimpleNamespace(name="Alice", total_score=100),
                   SimpleNamespace(name="Bob", total_score=50)]
        scoreboard.update_score("Alice", players)
        scoreboard.update_score("Bob", players)
        with open(scoreboard.SCORE_FILE) as f:
            data = json.load(f)
        counts = {p["name"]: p for p in data["players"].values()}
        self.assertEqual(counts["Alice"]["wins"], 1)
        self.assertEqual(counts["Alice"]["losses"], 1)
        self.assertEqual(counts["Alice"]["games"], 2)
        self.assertEqual(counts["Bob"]["wins"], 1)
        self.assertEqual(counts["Bob"]["losses"], 1)
        self.assertEqual(counts["Bob"]["games"], 2)

    def test_update_score_name_change(self):
        from types import SimpleNamespace
        players = [SimpleNamespace(name="Charlie", total_score=100)]
        scoreboard.update_score("Charlie", players)
        players[0].name = "CharlieNew"
        scoreboard.update_score("CharlieNew", players)
        with open(scoreboard.SCORE_FILE) as f:
            data = json.load(f)
        names = [p["name"] for p in data["players"].values()]
        self.assertIn("Charlie", names)
        self.assertIn("CharlieNew", names)

    def test_update_score_single_player_loss(self):
        from types import SimpleNamespace
        players = [SimpleNamespace(name="Alice", total_score=10),
                   SimpleNamespace(name="Bob", total_score=5)]
        scoreboard.update_score("Bob", players)
        with open(scoreboard.SCORE_FILE) as f:
            data = json.load(f)
        counts = {p["name"]: p for p in data["players"].values()}
        self.assertEqual(counts["Bob"]["wins"], 1)
        self.assertEqual(counts["Bob"]["losses"], 0)
        self.assertEqual(counts["Alice"]["wins"], 0)
        self.assertEqual(counts["Alice"]["losses"], 1)

    def test_update_score_creates_file_if_missing(self):
        # Ensure file does not exist
        if os.path.exists(scoreboard.SCORE_FILE):
            os.remove(scoreboard.SCORE_FILE)
        from types import SimpleNamespace
        players = [SimpleNamespace(name="Alice", total_score=50)]
        scoreboard.update_score("Alice", players)
        self.assertTrue(os.path.exists(scoreboard.SCORE_FILE))
        with open(scoreboard.SCORE_FILE) as f:
            data = json.load(f)
        names = [p["name"] for p in data["players"].values()]
        self.assertIn("Alice", names)

    # -------------------------
    # show_scores
    # -------------------------
    @patch("builtins.print")
    def test_show_scores_no_data(self, mock_print):
        with open(scoreboard.SCORE_FILE, "w") as f:
            json.dump({"players": {}}, f)
        scoreboard.show_scores()
        mock_print.assert_any_call("No scores yet!")

    @patch("builtins.print")
    def test_show_scores_with_data(self, mock_print):
        with open(scoreboard.SCORE_FILE, "w") as f:
            json.dump({"players": {
                "id1":{"name":"Alice","games":3,"wins":2,"losses":1},
                "id2":{"name":"Bob","games":2,"wins":0,"losses":2}
            }}, f)
        scoreboard.show_scores()
        mock_print.assert_any_call("\n🏅 High Scores 🏅")
        printed_names = [args[0] for args, _ in mock_print.call_args_list if "Alice" in args[0] or "Bob" in args[0]]
        self.assertTrue(any("Alice" in line for line in printed_names))
        self.assertTrue(any("Bob" in line for line in printed_names))

    @patch("builtins.print")
    def test_show_scores_multiple_players(self, mock_print):
        with open(scoreboard.SCORE_FILE, "w") as f:
            json.dump({"players": {
                "id1":{"name":"Alice","games":3,"wins":2,"losses":1},
                "id2":{"name":"Bob","games":2,"wins":0,"losses":2}
            }}, f)
        scoreboard.show_scores()
        printed_names = [args[0] for args, _ in mock_print.call_args_list]
        self.assertTrue(any("Alice: 2 wins / 1 losses / 3 games" in line for line in printed_names))
        self.assertTrue(any("Bob: 0 wins / 2 losses / 2 games" in line for line in printed_names))

if __name__ == "__main__":
    unittest.main()
